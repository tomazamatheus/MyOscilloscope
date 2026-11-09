import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDial, QLabel
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtCore import Qt


class Knob(QDial):
    def __init__(self, associatedClass, xcoord, ycoord, width, height, imagePath,
                 botlim, toplim, knobType, minUsefulValue, maxUsefulValue, incrementValue):
        super().__init__(associatedClass)
        self.associatedClass = associatedClass
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.width_ = width
        self.height_ = height
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

        # Criar dial
        self.setGeometry(self.xcoord, self.ycoord, self.width_, self.height_)  # posição e tamanho fixos
        self.setRange(self.botlim, self.toplim)
        self.setValue(self.botlim)
        self.setWrapping(True)
        self.lower()
        

        # Criar label para imagem (sobre o dial)
        self.label = QLabel(self)
        self.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("background-color: transparent;")


        # Carregar imagem original
        self.original_pixmap = QPixmap(self.imagePath)  # substitua pelo caminho da sua imagem

        # Conectar dial
        self.valueChanged.connect(self.rotate_image)


        # Chamar função create() para inicializar a imagem
        self.create()

    def create(self):
        """Configura a imagem inicial já sobre o dial"""
        # Redimensionar imagem para caber no dial
        self.scaled_pixmap = self.original_pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        #Exibir imagem inicial já alinhada ao dial
        self.rotate_image(self.value())

    def rotate_image(self, value):
        """Rotaciona a imagem conforme valor do dial"""
        angle = (value - self.botlim) * (360 / (self.toplim - self.botlim))
        transform = QTransform().rotate(angle)
        rotated_pixmap = self.scaled_pixmap.transformed(transform, Qt.TransformationMode.SmoothTransformation)

        # Atualizar label com a imagem rotacionada
        self.label.setPixmap(rotated_pixmap)

        # Centralizar a imagem sobre o dial
        dial_rect = self.geometry()
        self.label.setGeometry(
            (self.width() - rotated_pixmap.width()) // 2,
            (self.height() - rotated_pixmap.height()) // 2,
            rotated_pixmap.width(),
            rotated_pixmap.height()
        )

        if self.knobType in ["Trigger", "Position", "Amplitude"]:
            if value > self.prevValue or (value == self.minimum() and self.prevValue == self.maximum()):
                if self.usefulValue < self.maxUsefulValue and not (self.prevValue < 0 and value > 0):
                    if self.buttonIsOn:
                        self.usefulValue += self.incrementValue
                        self.pointerLevelUp = True

            if value < self.prevValue or (value == self.maximum() and self.prevValue == self.minimum()):
                if self.usefulValue > self.minUsefulValue and not (self.prevValue > 0 and value < 0):
                    if self.buttonIsOn:
                        self.usefulValue -= self.incrementValue
                        self.pointerLevelDown = True

        elif self.knobType in ["Time", "V/div"]:
            if value > self.prevValue or (value == self.minimum() and self.prevValue == self.maximum()):
                if self.usefulValue < self.maxUsefulValue:
                    if self.buttonIsOn:
                        self.usefulValue += self.incrementValue

            if value < self.prevValue or (value == self.maximum() and self.prevValue == self.minimum()):
                if self.usefulValue > self.minUsefulValue:
                    if self.buttonIsOn:
                        self.usefulValue -= self.incrementValue

            scale_map = {
                -9: 0.001, -8: 0.002, -7: 0.005, -6: 0.01, -5: 0.02, -4: 0.05, -3: 0.1, -2: 0.2, -1: 0.5,
                 0: 1, 1: 2, 2: 5, 3: 10, 4: 20, 5: 50
            }
            if self.usefulValue in scale_map:
                self.scaleValue = scale_map[self.usefulValue]

        elif self.knobType == "Cursor":
            if value > self.prevValue or (value == self.minimum() and self.prevValue == self.maximum()):
                if self.usefulValue < self.maxUsefulValue:
                    if self.buttonIsOn:
                        self.levelUp = True

            if value < self.prevValue or (value == self.maximum() and self.prevValue == self.minimum()):
                if self.usefulValue > self.minUsefulValue:
                    if self.buttonIsOn:
                        self.levelDown = True

        self.prevValue = value

    def changeImage(self, newImageName):
        self.imagePath = newImageName
        self.original_pixmap = QPixmap(self.imagePath)
        self.create()
        self.rotate_image(self.value())
