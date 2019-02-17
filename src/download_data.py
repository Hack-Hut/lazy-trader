"""
Used for downloading data from QUANDL and other such API's
"""

import csv
import os
import threading
from datetime import datetime

from iexfinance.stocks import get_historical_data
from iexfinance.utils.exceptions import IEXSymbolError, IEXEndpointError

import pandas as pd

INSTRUMENT_LIST = "../other/CSV/instrument_list.csv"

class FetchData():
	def __init__(self, LazyTrader):
		self.df_loc = "../df/asset"
		self.dict_list = []
		self.quandl_list = [] 
		self.iex_list = [] 
		self.LT = LazyTrader
		self.thread_count = 50

		self.completed = 0
		self.total = 0 

		self.fetch()

	def fetch(self):
		"""
		Used to download the data using API
		"""
		# Get metadata from CSV
		self.LT.Console.append("starting", "success")
		self.read_instruments()
		self.sort_api_list()

		# Download the data using the metadata
		self.thread_fetch_iex()
		self.fetch_qunadl()

		self.LT.Console.append("instruments avaliable: \t" + str(len(self.dict_list)))

	def sort_api_list(self):
		"""
		sorts through CSV data and adds the relevent instruments to correct list 
		"""
		for lines in self.dict_list:
			self.LT.Console.append(str(lines))
			if lines["API"] == "IEX":
				self.iex_list.append(lines)
			elif lines["API"] == "qunadl":
				self.quandl_list.append(lines)

	def exists(self, path):
		"""
		Checks if the path exists
		Args:
			path: path location
		"""
		if os.path.exists(path):
			return True
		else:
			self.LT.Console.append("CSV not found at the location " + INSTRUMENT_LIST, "error" )    
			return False

	def read_instruments(self):
		"""
		Reads the instrument list are saved in a csv.
		"""
		if self.exists(INSTRUMENT_LIST):
			with open(INSTRUMENT_LIST, "r") as infile:
				reader = csv.DictReader(infile)
				for line in reader:
					self.dict_list.append(line)
			return True
		return False

	def thread_fetch_iex(self):
		"""
		We have a list of tickers from our CSV, now we want to create a threadpool and itterate over that threadpool
		each time downloading the stock data to disk via the IEX module. Could think of a clean way to do this :/ 
		"""

		# Create neat list of stocks
		list_of_stocks = []
		for x in range(0, len(self.iex_list)):
			list_of_stocks.append(self.iex_list[x]["Plus-Ticker"])

		previous = 0 
		self.total = len(list_of_stocks)

		# Itterate over list with the thread count step 
		for x in range(self.thread_count, len(list_of_stocks), self.thread_count):
			stock_thread_pool = list_of_stocks[previous:x]
			self.start_thread(stock_thread_pool)
			
		# Round up the remaing stocks missed by the for loop step 
		if (self.total - previous - self.thread_count) < 0:
			get = self.total - previous
			stock_thread_pool = list_of_stocks[previous:self.total]
			self.start_thread(stock_thread_pool)


	def start_thread(self, stock_thread_pool):
		"""
		Create and execute N new threads, where n is len(stock_thread_pool). 
		Each thread downloads the ticker information		
		Args:
		    stock_thread_pool (list): contains tickers to download 
		"""
		threads = [threading.Thread(target=self.iex_wrapper, args=(stock,)) for stock in stock_thread_pool]
		for thread in threads:
			thread.start()
		for thread in threads:
			thread.join()
		print("threads finished")

	def iex_wrapper(self, ticker, n=False):
		"""
		Wrapper for IEX incase API changes in the future. Save the ticker info as a 
		pickle in a pandas format in the output dir 
		"""
		try:
			path = os.path.join(self.df_loc, ticker)
			start = datetime(2017, 1, 1)
			end = datetime(2018, 1, 1)
			df = get_historical_data(ticker, output_format='pandas')
			df.to_pickle(path.strip(" "))
			print(ticker + " found")

		except IEXSymbolError as e:
			print(ticker + "not found")
			self.LT.Console.append(ticker + " not found", error)

		self.completed += 1
		self.progress_bar()


	def progress_bar(self):
		"""
		Updates the progress bar
		"""
		print(self.completed)
		print(self.total)
		print("\n")
		value = (self.completed / self.total) * 100
		self.LT.progressBar.setValue(value)
