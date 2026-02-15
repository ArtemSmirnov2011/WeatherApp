from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame

class TimeInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setFixedSize(390, 303)
        self.setStyleSheet("""
                    background-color: rgba(0, 0, 0, 0.2);
                    border-radius: 20px
                    """)
        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()

        self.today = QLabel("Сьогодні")
        self.today.setFont(QFont("Arial", 15))
        self.today.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.today.setStyleSheet("background-color: transparent")
        self.today.setFixedSize(100, 50)
        self.today.setContentsMargins(15, 15, 0, 0)
        self.layout1.addWidget(self.today)
        
        self.day = QLabel("Субота")
        self.day.setFont(QFont("Arial", 20))
        self.day.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.day.setStyleSheet("background-color: transparent")
        self.day.setFixedHeight(50)
        self.day.setContentsMargins(15, 0, 0, 0)
        self.layout2.addWidget(self.day)
        
        self.date = QLabel("14.02.2026")
        self.date.setFont(QFont("Arial", 20))
        self.date.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.date.setStyleSheet("background-color: transparent")
        self.date.setFixedHeight(50)
        self.date.setContentsMargins(0, 0, 15, 0)
        self.layout2.addWidget(self.date)

        self.time = QLabel("12:00")
        self.time.setFont(QFont("Arial", 30))
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time.setStyleSheet("background-color: transparent")
        self.layout3.addWidget(self.time)

        self.setLayout(self.layout1)
        self.layout1.addLayout(self.layout2)
        self.layout1.addLayout(self.layout3)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2)")