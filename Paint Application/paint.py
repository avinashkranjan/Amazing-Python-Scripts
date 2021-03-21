# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys 

# window class 
class Window(QMainWindow): 
	def __init__(self): 
		super().__init__() 

		# setting application window up 
		self.setWindowTitle("Paint with PyQt5")
		self.setGeometry(100, 100, 800, 600) 

		# setting up image object 
		self.image = QImage(self.size(), QImage.Format_RGB32) 
		self.image.fill(Qt.white) 

		# variables 
		# drawing flag - shows if currently drawing 
		self.drawing = False
		self.brushSize = 2
		self.brushColor = Qt.black 
		# QPoint object to track the point of cursor release
		self.lastPoint = QPoint() 

		# creating menu bar 
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu("File")
		b_size = mainMenu.addMenu("Brush Size")
		b_color = mainMenu.addMenu("Brush Color") 

		# creating save action 
		saveAction = QAction("Save", self)
		saveAction.setShortcut("Ctrl + S") 
		fileMenu.addAction(saveAction)
		saveAction.triggered.connect(self.save) 

		# creating clear action 
		clearAction = QAction("Clear", self)
		clearAction.setShortcut("Ctrl + C")
		fileMenu.addAction(clearAction)
		clearAction.triggered.connect(self.clear) 

		# creating options for brush sizes 
		pix_4 = QAction("4px", self)
		b_size.addAction(pix_4)
		pix_4.triggered.connect(self.Pixel_4) 

		pix_7 = QAction("7px", self) 
		b_size.addAction(pix_7) 
		pix_7.triggered.connect(self.Pixel_7) 

		pix_9 = QAction("9px", self) 
		b_size.addAction(pix_9) 
		pix_9.triggered.connect(self.Pixel_9) 

		pix_12 = QAction("12px", self) 
		b_size.addAction(pix_12) 
		pix_12.triggered.connect(self.Pixel_12) 

		# creating options for brush color
		black = QAction("Black", self)  
		b_color.addAction(black) 
		black.triggered.connect(self.blackColor) 

		white = QAction("White", self) 
		b_color.addAction(white) 
		white.triggered.connect(self.whiteColor) 

		green = QAction("Green", self) 
		b_color.addAction(green) 
		green.triggered.connect(self.greenColor) 

		yellow = QAction("Yellow", self) 
		b_color.addAction(yellow) 
		yellow.triggered.connect(self.yellowColor) 

		red = QAction("Red", self) 
		b_color.addAction(red) 
		red.triggered.connect(self.redColor) 


	# method for checking mouse clicks 
	def mousePressEvent(self, event): 

		# if left mouse button is pressed 
		if event.button() == Qt.LeftButton: 
			# set drawing flag true 
			self.drawing = True
			# set last point to the point of cursor 
			self.lastPoint = event.pos() 

	# method for tracking mouse activity (enables drawing)
	def mouseMoveEvent(self, event): 
		
		# checking if left button is pressed and drawing flag is true 
		if (event.buttons() & Qt.LeftButton) & self.drawing: 
			
			# creating painter object 
			painter = QPainter(self.image) 			
			# set the pen of the painter 
			painter.setPen(QPen(self.brushColor, self.brushSize, 
							Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)) 			
			# draw line from the last point of cursor to the current point 
			painter.drawLine(self.lastPoint, event.pos())
			self.lastPoint = event.pos()
			self.update() 

	# method for mouse left button release 
	def mouseReleaseEvent(self, event): 

		if event.button() == Qt.LeftButton: 
			# make drawing flag false 
			self.drawing = False

	# paint event 
	def paintEvent(self, event): 
		# create a canvas 
		canvasPainter = QPainter(self)
		canvasPainter.drawImage(self.rect(), self.image, self.image.rect()) 

	# method for saving canvas 
	def save(self): 
		filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", 
						"PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ") 
		if filePath == "": 
			return
		self.image.save(filePath) 

	# method for clearing canvas 
	def clear(self): 
		# make the whole canvas white 
		self.image.fill(Qt.white)  
		self.update() 

	# methods for changing pixel sizes 
	def Pixel_4(self): 
		self.brushSize = 4

	def Pixel_7(self): 
		self.brushSize = 7

	def Pixel_9(self): 
		self.brushSize = 9

	def Pixel_12(self): 
		self.brushSize = 12

	# methods for changing brush color 
	def blackColor(self): 
		self.brushColor = Qt.black 

	def whiteColor(self): 
		self.brushColor = Qt.white 

	def greenColor(self): 
		self.brushColor = Qt.green 

	def yellowColor(self): 
		self.brushColor = Qt.yellow 

	def redColor(self): 
		self.brushColor = Qt.red 



# create pyqt5 app 
App = QApplication(sys.argv) 

# create the instance of our Window 
window = Window() 
window.show() 

# start the app 
sys.exit(App.exec()) 
