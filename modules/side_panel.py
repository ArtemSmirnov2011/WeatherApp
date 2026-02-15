from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QScrollArea, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QScrollArea, QLabel
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QScrollArea, QLabel
from PyQt6.QtCore import Qt

class SidePanel(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.2);
            border: 0
        """)

        self.setFixedSize(370, 800)
        self.main_layout = QVBoxLayout()
        self.scroll_element = QScrollArea(self)
        self.scroll_element.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_element)
        self.scroll_element.setFixedSize(370, 800)
        self.scroll_element.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.vertical_layout = QVBoxLayout()
        self.content = QFrame()
        self.content.setLayout(self.vertical_layout)
        
        for num in range(10):
            frame = QFrame()

            self.layout1 = QVBoxLayout()
            self.layout2 = QHBoxLayout()
            self.layout3 = QVBoxLayout()
            self.city_name = QLabel("Дніпро")
            self.city_name.setFont(QFont("Arial", 20, QFont.Weight.Bold))
            self.city_name.setFixedSize(100, 50)
            self.city_name.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.layout1.addWidget(self.city_name)

            self.time = QLabel("12:00")
            self.time.setFont(QFont("Arial", 12))
            self.time.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.time.setFixedSize(100, 50)
            self.layout1.addWidget(self.time)
            
            self.description = QLabel("Сонячно")
            self.description.setFont(QFont("Arial", 12))
            self.description.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.layout2.addWidget(self.description)
            
            self.temp = QLabel("25°C")
            self.temp.setFont(QFont("Arial", 25))
            self.temp.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.temp.setFixedSize(100, 50)

            self.temp.setContentsMargins(0, 0, 0, 0)
            self.layout3.addWidget(self.temp)
        
            self.max_temp = QLabel("Макс.: 30°C")
            self.max_temp.setFont(QFont("Arial", 12))
            self.max_temp.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.layout2.addWidget(self.max_temp)

            self.min_temp = QLabel("Мін.: 20°C")
            self.min_temp.setFont(QFont("Arial", 12))
            self.min_temp.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.layout2.addWidget(self.min_temp)
            
            frame.setLayout(self.layout1)
            self.layout1.addLayout(self.layout3)
            self.layout1.addLayout(self.layout2)
            frame.setFixedSize(300, 200)

            frame.setFixedSize(300, 200)
            frame.setStyleSheet("""
                    background-color: transparent;
                    """)
            self.vertical_layout.addWidget(frame)

        self.scroll_element.setWidget(self.content)
        