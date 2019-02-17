class ConsoleLog:
	def __init__(self, txt_browser):
		self.txt_browser = txt_browser
		self.DEBUG = "#0e16f4"		# Blue
		self.ERROR =  "#ba0000"		# Red
		self.WARNING = "#ba6000"	# Orange
		self.SUCCCES = "#0fc433"	# Green
		self.NORMAL = "#ffffff"		# White
		self.banner()

	def append(self, text, color="success"):
		print("text")
		col = self.color_picker(color)
		msg = "<span style=\" font-size:9pt; font-weight:400; color:" + col
		msg += text
		msg += "</span>"
		self.txt_browser.append(msg)

	def color_picker(self, color):
		if color  == "debug":
			return self.DEBUG + ";\" > [ ]\t\t---" 
		if color  == "error":
			return self.ERROR + ";\" > [!]\t\t---"	
		if color  == "warning":
			return self.WARNING + ";\" > [-]\t\t---"
		if color  == "success":
			return self.SUCCCES + ";\" > [+]\t\t---"
		if color  == "normal":
			return self.NORMAL	+ ";\" >\t\t---"
		else:
			return self.NORMAL	+ ";\" >\t\t---"
			self.txt_browser.append("Color picker failed\n Selected color was: \t" + color)

	def banner(self):
		self.banner = ""
		self.banner += "  _____     ____\t             ______                 \n"
		self.banner += " /         \\  |  o | \t|    _. _ __   | ._ _.  _|  _  ._ \n"
		self.banner += "|           |/ ___\\| \t|_ (_| /_ \\/ --| | (_| (_| (/_ |  \n"
		self.banner += "|_________/           \t            /                     \n"
		self.banner += "|_|_| |_|_| \t\t________________________\n"
		self.txt_browser.append(self.banner)