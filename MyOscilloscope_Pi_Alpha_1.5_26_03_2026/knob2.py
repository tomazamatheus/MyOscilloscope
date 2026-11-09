import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QDial
from PyQt6.QtGui import QPixmap, QTransform
from PyQt6.QtCore import Qt


class Knob(QDial):
    def __init__(self, associatedClass, xcoord, ycoord, width, height, imagePath,
                 botlim, toplim, knobType, minUsefulValue, maxUsefulValue, incrementValue):
        super().__init__(associatedClass)
        self.associatedClass = associatedClass
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.width = width
        self.height = height
        self.imagePath = imagePath
        self.botlim = botlim
        self.toplim = toplim
        self.knobType = knobType
        self.usefulValue = 0
        self.minUsefulValue = minUsefulValue
        self.maxUsefulValue = maxUsefulValue
        self.incrementValue = incrementValue

        # atributos auxiliares
        self.scaleValue = 1
        self.pointerLevelUp = False
        self.pointerLevelDown = False
        self.prevValue = 0
        self.buttonIsOn = False
        self.levelUp = False
        self.levelDown = False

        #criando o dial:
        self.setGeometry(self.xcoord, self.ycoord, self.width, self.height)
        self.setRange(self.botlim, self.toplim)
        self.setValue(0)

        #Label da imagem:
        self.label = QLabel(self)
        self.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.valueChanged.connect(self.rotate_image)
        self.create()

    def create(self):
        self.scaled_pixmap = QPixmap(self.imagePath).scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.label.setPixmap(self.scaled_pixmap)
        self.rotate_image(self.value())

    def rotate_image(self, value):
        angle = (value - self.botlim) * (360 / (self.toplim - self.botlim))
        transform = QTransform().rotate(angle)
        rotated_pixmap = self.scaled_pixmap.transformed(transform, Qt.TransformationMode.SmoothTransformation)

        # Atualizar label com a imagem rotacionada
        self.label.setPixmap(rotated_pixmap)

        # Centralizar a imagem sobre o dial
        # dial_rect = self.geometry()
        # self.label.setGeometry(
        #     dial_rect.x() + (dial_rect.width() - rotated_pixmap.width()) // 2,
        #     dial_rect.y() + (dial_rect.height() - rotated_pixmap.height()) // 2,
        #     rotated_pixmap.width(),
        #     rotated_pixmap.height()
        # )


class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Teste do Knob")
        self.setFixedSize(400, 400)

        # Criação do knob
        self.knob = Knob(
            associatedClass=self,
            xcoord=110,
            ycoord=110,
            width=180,
            height=180,
            imagePath="images/Knob1.png",
            botlim=-10,
            toplim=10,
            knobType="Time",
            minUsefulValue=-6,
            maxUsefulValue=5,
            incrementValue=1
        )


# ===== MAIN =====
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TestWindow()
    win.show()
    sys.exit(app.exec())