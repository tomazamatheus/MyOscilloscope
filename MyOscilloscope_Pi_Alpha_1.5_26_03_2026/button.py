from PySide6.QtWidgets import QPushButton, QLabel
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import Qt
from pathlib import Path


class Button(QPushButton):
    def __init__(
        self,
        parent,
        x,
        y,
        width,
        height,
        name,
        image_off,
        image_on,
        is_on=False
    ):
        super().__init__(parent)

        self.parent = parent
        self.name = name
        self.isOn = is_on

        self.image_off_path = image_off
        self.image_on_path = image_on

        self.setGeometry(x, y, width, height)

        self._setup_button()
        self._setup_visual()

        self.clicked.connect(self.toggle_state)

    # --------------------------------------------------

    def _setup_button(self):
        self.setText(self.name)

        self.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
            }
            QPushButton:hover,
            QPushButton:pressed,
            QPushButton:focus {
                background-color: transparent;
                border: none;
                outline: none;
            }
        """)

    # --------------------------------------------------

    def _setup_visual(self):
        suffix = Path(self.image_off_path).suffix.lower()

        self.visual = None
        self.visual_type = None  # "svg" ou "pixmap"

        if suffix == ".svg":
            self.visual_type = "svg"
            self.visual = QSvgWidget(self.parent)
            self.visual.setGeometry(self.geometry())
            self.visual.setStyleSheet("background-color: transparent;")
            self.visual.setAttribute(
                Qt.WidgetAttribute.WA_TransparentForMouseEvents, True
            )

        else:
            self.visual_type = "pixmap"
            self.visual = QLabel(self.parent)
            self.visual.setGeometry(self.geometry())
            self.visual.setStyleSheet("background-color: transparent;")
            self.visual.setAttribute(
                Qt.WidgetAttribute.WA_TransparentForMouseEvents, True
            )

        self._update_visual()

    # --------------------------------------------------

    def _update_visual(self):
        path = self.image_on_path if self.isOn else self.image_off_path

        if self.visual_type == "svg":
            self.visual.load(path)

        elif self.visual_type == "pixmap":
            pix = QPixmap(path)
            if not pix.isNull():
                self.visual.setPixmap(
                    pix.scaled(
                        self.visual.size(),
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                )

    # --------------------------------------------------

    def toggle_state(self):
        self.isOn = not self.isOn
        self._update_visual()

    # --------------------------------------------------

    def moveButton(self, x, y):
        self.move(x, y)
        self.visual.move(x, y)
