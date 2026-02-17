from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame

class WeatherInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setFixedSize(390, 303)

        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()

        self.city_name = QLabel("Дніпро")
        self.city_name.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.city_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_name.setStyleSheet("background-color: transparent")
        self.city_name.setContentsMargins(0, 30, 0, 0)
        self.layout1.addWidget(self.city_name)

        self.weather_image = QPixmap("images/weather.svg")
        self.weather_image = self.weather_image.scaled(170, 170)
       
        self.weather_image_label = QLabel()
        self.weather_image_label.setPixmap(self.weather_image)
        self.weather_image_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.weather_image_label.setStyleSheet("background-color: transparent")
        self.weather_image_label.setFixedSize(375, 190)
        self.weather_image_label.setContentsMargins(50, 0, 20, 30)
        self.weather_image_label.setLayout(self.layout3)
        self.layout1.addWidget(self.weather_image_label)

        self.temp = QLabel("25°C")
        self.temp.setFont(QFont("Arial", 45))  
        self.temp.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.temp.setStyleSheet("background-color: transparent")
        self.temp.setContentsMargins(0, 40, 0, 0)
        self.layout3.addWidget(self.temp)

        self.description = QLabel("Сонячно")
        self.description.setFont(QFont("Arial", 14))
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description.setStyleSheet("background-color: transparent")
        self.description.setContentsMargins(0, 50, 0, 0)
        self.layout1.addWidget(self.description)

        self.temp_max = QLabel("Макс.: 30°C")
        self.temp_max.setFont(QFont("Arial", 12))
        self.temp_max.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.temp_max.setStyleSheet("background-color: transparent")
        self.temp_max.setContentsMargins(100, 20, 0, 0)
        self.layout2.addWidget(self.temp_max)

        self.temp_min = QLabel("Мін.: 20°C")
        self.temp_min.setFont(QFont("Arial", 12))
        self.temp_min.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.temp_min.setStyleSheet("background-color: transparent")
        self.temp_min.setContentsMargins(0, 20, 100, 0)
        self.layout2.addWidget(self.temp_min)

        self.setLayout(self.layout1)
        self.layout1.addLayout(self.layout2)
        self.layout1.addLayout(self.layout3)
        self.setStyleSheet("""
                        background-color: rgba(0, 0, 0, 0.2);
                        border-radius: 20px;
        """)