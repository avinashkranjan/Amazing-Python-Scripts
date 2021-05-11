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
        self.setWindowTitle("Paint Application")
        self.setGeometry(100, 100, 800, 600)

        # setting up image object
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        # variables
        # drawing flag - shows if currently drawing
        self.drawing = False

        # brush specifications
        self.brushSize = 2
        self.brushColor = Qt.black
        self.brushStyle = Qt.SolidLine

        # QPoint object to track the point of cursor release
        self.lastPoint = QPoint()

        # creating menu bar
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        brush_size = mainMenu.addMenu("Brush Size")
        brush_color = mainMenu.addMenu("Brush Color")
        canvas_color = mainMenu.addMenu("Canvas Color")
        brush_style = mainMenu.addMenu("Brush Style")

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
        brush_size.addAction(pix_4)
        pix_4.triggered.connect(self.Pixel_4)

        pix_7 = QAction("7px", self)
        brush_size.addAction(pix_7)
        pix_7.triggered.connect(self.Pixel_7)

        pix_9 = QAction("9px", self)
        brush_size.addAction(pix_9)
        pix_9.triggered.connect(self.Pixel_9)

        pix_12 = QAction("12px", self)
        brush_size.addAction(pix_12)
        pix_12.triggered.connect(self.Pixel_12)

        # creating options for brush color
        black = QAction("Black", self)
        brush_color.addAction(black)
        black.triggered.connect(self.blackColor)

        white = QAction("White", self)
        brush_color.addAction(white)
        white.triggered.connect(self.whiteColor)

        green = QAction("Green", self)
        brush_color.addAction(green)
        green.triggered.connect(self.greenColor)

        yellow = QAction("Yellow", self)
        brush_color.addAction(yellow)
        yellow.triggered.connect(self.yellowColor)

        red = QAction("Red", self)
        brush_color.addAction(red)
        red.triggered.connect(self.redColor)

        # Creating Canvas colors
        red_canvas = QAction("Red", self)
        canvas_color.addAction(red_canvas)
        red_canvas.triggered.connect(self.redCanvas)

        black_canvas = QAction("Black", self)
        canvas_color.addAction(black_canvas)
        black_canvas.triggered.connect(self.blackCanvas)

        yellow_canvas = QAction("Yellow", self)
        canvas_color.addAction(yellow_canvas)
        yellow_canvas.triggered.connect(self.yellowCanvas)

        green_canvas = QAction("Green", self)
        canvas_color.addAction(green_canvas)
        green_canvas.triggered.connect(self.greenCanvas)

        white_canvas = QAction("White", self)
        canvas_color.addAction(white_canvas)
        white_canvas.triggered.connect(self.whiteCanvas)

        # Creating Brush styles
        solid_brush = QAction("Solid", self)
        brush_style.addAction(solid_brush)
        solid_brush.triggered.connect(self.solidBrush)

        dot_brush = QAction("Dot", self)
        brush_style.addAction(dot_brush)
        dot_brush.triggered.connect(self.dotBrush)

        dash_brush = QAction("Dash", self)
        brush_style.addAction(dash_brush)
        dash_brush.triggered.connect(self.dashBrush)

        dashDot_brush = QAction("Dash Dot", self)
        brush_style.addAction(dashDot_brush)
        dashDot_brush.triggered.connect(self.dashDotBrush)

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
                                self.brushStyle, Qt.RoundCap, Qt.RoundJoin))
            # draw line from the last point
            # of cursor to the current point
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

    # methods for changing canvas color
    def redCanvas(self):
        self.image.fill(Qt.red)
        red_msg = QMessageBox()
        red_msg.setText("Canvas color changed to Red!")
        x = red_msg.exec_()

    def blackCanvas(self):
        self.image.fill(Qt.black)
        black_msg = QMessageBox()
        black_msg.setText("Canvas color changed to Black!")
        x = black_msg.exec_()

    def yellowCanvas(self):
        self.image.fill(Qt.yellow)
        yellow_msg = QMessageBox()
        yellow_msg.setText("Canvas color changed to yellow!")
        x = yellow_msg.exec_()

    def greenCanvas(self):
        self.image.fill(Qt.green)
        green_msg = QMessageBox()
        green_msg.setText("Canvas color changed to green!")
        x = green_msg.exec_()

    def whiteCanvas(self):
        self.image.fill(Qt.white)
        white_msg = QMessageBox()
        white_msg.setText("Canvas color changed to white!")
        x = white_msg.exec_()

    # methods to change brush style
    def solidBrush(self):
        self.brushStyle = Qt.SolidLine

    def dotBrush(self):
        self.brushStyle = Qt.DotLine

    def dashBrush(self):
        self.brushStyle = Qt.DashLine

    def dashDotBrush(self):
        self.brushStyle = Qt.DashDotLine


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
window.show()

# start the app
sys.exit(App.exec())
