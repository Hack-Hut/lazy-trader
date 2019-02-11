import matplotlib 
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import matplotlib.animation as animation 
from matplotlib import style 

LARGE_FONT = ("sadf", 42)
style.use("seaborn-darkgrid")

class LazyTrader(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		self.frames = {}

		for F in (StartPage, PageOne, PageThree):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
		
		self.show_frame(StartPage)


	def show_frame(self, cont):
		frame = self.frames[cont]
		print(cont)
		frame.tkraise()

def qf(param):
	print(param)
	

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self, text="Vist Page 1",
							command=lambda: controller.show_frame(PageOne))
		button1.pack()

		button3 = ttk.Button(self, text="Graph page",
							command=lambda: controller.show_frame(PageThree))
		button3.pack()


class PageOne(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Page One", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self, text="Back to home", command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = ttk.Button(self, text="Page One", command=lambda: controller.show_frame(StartPage))
		button2.pack()

		button3 = ttk.Button(self, text="Page two", command=lambda: controller.show_frame(StartPage))
		button3.pack()


class PageTwo(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button1 = tk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = tk.Button(self, text="Page One",
							command=lambda: controller.show_frame(PageOne))
		button2.pack()

class PageThree(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Graph page!!!", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button1 = tk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.pack()

		f = Figure(figsize=(5,5), dpi=100)
		a = f.add_subplot(111)
		a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		toolbar = NavigationToolbar2Tk(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		

app = LazyTrader()
app.mainloop()
