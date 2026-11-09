import sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class Standby(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(10, 260, 1120, 360)
        self.label = QLabel(self)
        self.label.setGeometry(self.rect())
        self.label.setScaledContents(True)
        self.pixmap1 = QPixmap("images/standbyImage.png")
        self.pixmap2 = QPixmap("images/standbyImage2.png")
        self.pixmap3 = QPixmap("images/standbyImage_PT.png")
        self.pixmap4 = QPixmap("images/standbyImage2_PT.png")

        
        self.updatePixmap(self.pixmap1)

    def updatePixmap(self, pixmap):
        self.label.setGeometry(0, 0, self.width(), self.height())
        if pixmap.isNull():
            return

        scaled = pixmap.scaled(
            self.label.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.label.setPixmap(scaled)



# app = QApplication(sys.argv)
# window = Standby()
# window.show()
# app.exec()