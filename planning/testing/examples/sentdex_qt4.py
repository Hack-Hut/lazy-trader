from PyQt4 import QtGui, QtCore
import qdarkgraystyle
import sys


class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		# Define window size 
		self.setGeometry(500,50,500,300)
		self.setWindowTitle("./Lazy-Trader")
		#self.setWindowIcon(QtGui.QIcon('test.png'))

		extractAction = QtGui.QAction("&Get TO THE CHOPPA!!!!", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip("Exit the application")
		extractAction.triggered.connect(self.close_application)

		# File, Edit etc
		self.statusBar()
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu("&File")
		fileMenu.addAction(extractAction)
		self.home()


	def home(self):
		btn = QtGui.QPushButton("Quit!", self)
		#btn.clicked.connect(QtCore.QCoreApplication.instance().quit())
		btn.clicked.connect(self.close_application)
		btn.resize(btn.sizeHint())
		btn.move(0, 100)

		# Toolbar
		# self.toolBar = self.addToolBar("Extraction")
		# self.toolBar.addAction()

		fontChoice = QtGui.QAction("font", self)
		fontChoice.triggered.connect(self.font_choice)
		self.toolBar = self.addToolBar("Font")
		self.toolBar.addAction(fontChoice)

		# checkBox
		checkbox = QtGui.QCheckBox('Enlarge Window', self)
		checkbox.move(100,25)
		checkbox.toggle()
		checkbox.stateChanged.connect(self.enlarge_window)

		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(200, 80, 250, 20)

		# Download button
		self.btn = QtGui.QPushButton("Download", self)
		self.btn.move(200, 120)
		self.btn.clicked.connect(self.download)

		print(self.style().objectName())
		self.styleChoice = QtGui.QLabel("Windows Vista", self)

		#
		comboBox = QtGui.QComboBox(self)
		comboBox.addItem("motif")
		comboBox.addItem("Windows")
		comboBox.addItem("cde")
		comboBox.addItem("Plastique")
		comboBox.addItem("cleanlooks")
		comboBox.addItem("windowsvista")

		comboBox.move(50, 250)
		self.styleChoice.move(50, 150)
		comboBox.activated[str].connect(self.style_choice)
		# 

		self.show()

	def font_choice(self):
		font, valid = QtGui.QFontDialog.getFont()
		if valid:
			self.styleChoice.setFont(font)

	def style_choice(self, text):
		# Change theme
		self.styleChoice.setText(text)
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

	def download(self):
		self.completed = 0	
		while self.completed < 100:
			self.completed += 0.0001
			self.progress.setValue(self.completed)

	def enlarge_window(self, state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50,50,500,600)
		else:
			self.setGeometry(50,50,1000,600)


	def close_application(self):
		# Yes No pop up 
		choice = QtGui.QMessageBox.question(self, "extract!", "Quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			print("Exiting")
			sys.exit()

def run():
	app = QtGui.QApplication(sys.argv)
	app.setStyleSheet(qdarkgraystyle.load_stylesheet())
	GUI = Window()
	sys.exit(app.exec_())	

run()