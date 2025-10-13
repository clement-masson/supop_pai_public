import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QSlider,
    QLineEdit,
    QCheckBox,
    QLabel,
)
from PySide6.QtCore import Qt, QTime, QTimer


class SinusWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Variables internes
        self.frequency = 1.0
        self.amplitude = 1.0
        self.phase = 0.0
        self.phase_increment = 0.1

        # Contrôles de la fréquence
        self.freq_slider = QSlider(Qt.Orientation.Horizontal)
        # Les QSlider ne prennent que des valeurs entieres, on divisera par 10 la valeur en Hertz ...
        self.freq_slider.setRange(1, 100)  # 0.1 à 10.0 Hz
        self.freq_slider.setValue(10)  # 1.0 Hz par défaut

        self.freq_text = QLineEdit("1.0")
        self.freq_text.setFixedWidth(60)

        freq_layout = QHBoxLayout()
        freq_layout.addWidget(self.freq_slider)
        freq_layout.addWidget(self.freq_text)
        freq_group = QGroupBox("Fréquence (Hz)")
        freq_group.setLayout(freq_layout)

        # Contrôles de l'amplitude
        # TODO

        # Contrôles de la phase
        # TODO

        # Controles de l'animation
        # TODO

        # Widget du Panneau de gauche regroupant tous les controles
        # TODO

        # Widget pour le graphique à droite
        # TODO

        # Layout principal
        # TODO

        # Initialisation du graphique
        self.update_figure()

    def update_figure(self):
        pass  #  TODO


def main():
    app = QApplication(sys.argv)
    window = SinusWidget()
    window.setWindowTitle("Graphique Sinus Interactif")
    window.setGeometry(100, 100, 800, 600)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
