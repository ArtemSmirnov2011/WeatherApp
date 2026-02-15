from PyQt6.QtWidgets import QFrame, QScrollArea, QHBoxLayout
from PyQt6.QtCore import Qt

class ForecastInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        self.setFixedSize(790, 157)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2)")

        self.scroll_element = QScrollArea(self)
        self.scroll_element.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_element)
        self.scroll_element.setFixedSize(790, 157)
        self.scroll_element.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.scroll_frame = QFrame()

        self.forecast_layout = QHBoxLayout()
        self.scroll_frame.setLayout(self.forecast_layout)


        for i in range(15):
            frame = QFrame()
            frame.setFixedSize(100, 100)
            frame.setStyleSheet("background-color: red")
            self.forecast_layout.addWidget(frame)

        self.scroll_element.setWidget(self.scroll_frame)