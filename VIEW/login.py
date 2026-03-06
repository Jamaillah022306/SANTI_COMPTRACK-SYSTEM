# Improved Login UI for Inventory System - Resizable
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit


class Ui_LoginForm(object):
    def setupUi(self, Form):
        Form.setObjectName("LoginForm")
        Form.resize(1280, 720)
        Form.setMinimumSize(600, 550)

        # ── Support both QMainWindow (controller) and QWidget (standalone test) ──
        if isinstance(Form, QtWidgets.QMainWindow):
            self.centralwidget = QtWidgets.QWidget(Form)
            Form.setCentralWidget(self.centralwidget)
            container = self.centralwidget
        else:
            container = Form

        container.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
            "stop:0 rgba(41, 128, 185, 255), stop:1 rgba(52, 152, 219, 255));"
        )

        # Outer layout to center the card both horizontally and vertically
        outer_layout = QVBoxLayout(container)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Main Login Frame (fixed size card, centered by layout)
        self.frame_login = QtWidgets.QFrame()
        self.frame_login.setFixedSize(420, 510)
        self.frame_login.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.95);
                border-radius: 15px;
            }
        """)
        self.frame_login.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_login.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_login.setObjectName("frame_login")

        # Inner layout for card contents
        card_layout = QVBoxLayout(self.frame_login)
        card_layout.setContentsMargins(50, 25, 50, 35)
        card_layout.setSpacing(10)
        card_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # Logo Image (above title)
        self.label_logo_image = QtWidgets.QLabel()
        self.label_logo_image.setFixedHeight(65)
        self.label_logo_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_logo_image.setStyleSheet("background: transparent;")
        self.label_logo_image.setObjectName("label_logo_image")
        logo_pixmap = QtGui.QPixmap(
            r"C:\Users\asus\PycharmProjects\Inventory_System_Final\SOURCE\logo.png"
        )
        if not logo_pixmap.isNull():
            self.label_logo_image.setPixmap(
                logo_pixmap.scaled(150, 60,
                                   QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                   QtCore.Qt.TransformationMode.SmoothTransformation)
            )
        card_layout.addWidget(self.label_logo_image)
        card_layout.addSpacing(5)

        # Title
        self.label_logo = QtWidgets.QLabel()
        self.label_logo.setStyleSheet(
            "color: rgb(41, 128, 185); font: bold 18pt 'Segoe UI'; background: transparent;"
        )
        self.label_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        card_layout.addWidget(self.label_logo)
        card_layout.addSpacing(6)

        # Subtitle
        self.label_subtitle = QtWidgets.QLabel()
        self.label_subtitle.setStyleSheet(
            "color: rgb(127, 140, 141); font: 10pt 'Segoe UI'; background: transparent;"
        )
        self.label_subtitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_subtitle.setObjectName("label_subtitle")
        card_layout.addWidget(self.label_subtitle)
        card_layout.addSpacing(22)

        # Username Label
        self.label_username = QtWidgets.QLabel()
        self.label_username.setStyleSheet(
            "color: rgb(52, 73, 94); font: bold 10pt 'Segoe UI'; background: transparent;"
        )
        self.label_username.setObjectName("label_username")
        card_layout.addWidget(self.label_username)
        card_layout.addSpacing(6)

        # Username Input
        self.input_username = QtWidgets.QLineEdit()
        self.input_username.setFixedHeight(45)
        self.input_username.setStyleSheet("""
            QLineEdit {
                background-color: rgb(236, 240, 241);
                border: 2px solid rgb(189, 195, 199);
                border-radius: 8px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: rgb(44, 62, 80);
            }
            QLineEdit:focus {
                border: 2px solid rgb(52, 152, 219);
            }
        """)
        self.input_username.setObjectName("input_username")
        card_layout.addWidget(self.input_username)
        card_layout.addSpacing(15)

        # Password Label
        self.label_password = QtWidgets.QLabel()
        self.label_password.setStyleSheet(
            "color: rgb(52, 73, 94); font: bold 10pt 'Segoe UI'; background: transparent;"
        )
        self.label_password.setObjectName("label_password")
        card_layout.addWidget(self.label_password)
        card_layout.addSpacing(6)

        # Password Input
        self.input_password = QtWidgets.QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setFixedHeight(45)
        self.input_password.setStyleSheet("""
            QLineEdit {
                background-color: rgb(236, 240, 241);
                border: 2px solid rgb(189, 195, 199);
                border-radius: 8px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: rgb(44, 62, 80);
            }
            QLineEdit:focus {
                border: 2px solid rgb(52, 152, 219);
            }
        """)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.input_password.setObjectName("input_password")
        card_layout.addWidget(self.input_password)
        card_layout.addSpacing(30)

        # Login Button
        self.btn_login = QtWidgets.QPushButton()
        self.btn_login.setFixedHeight(50)
        self.btn_login.setStyleSheet("""
            QPushButton {
                background-color: rgb(52, 152, 219);
                color: white;
                border: none;
                border-radius: 8px;
                font: bold 12pt 'Segoe UI';
            }
            QPushButton:hover {
                background-color: rgb(41, 128, 185);
            }
            QPushButton:pressed {
                background-color: rgb(31, 97, 141);
            }
        """)
        self.btn_login.setObjectName("btn_login")
        card_layout.addWidget(self.btn_login)

        outer_layout.addWidget(self.frame_login)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("LoginForm", "Inventory System - Login"))
        self.label_logo.setText(_translate("LoginForm", "COMPUTER INVENTORY"))
        self.label_subtitle.setText(_translate("LoginForm", "Welcome and have a wonderful day!"))
        self.label_username.setText(_translate("LoginForm", "Username"))
        self.input_username.setPlaceholderText(_translate("LoginForm", "Enter your username"))
        self.label_password.setText(_translate("LoginForm", "Password"))
        self.input_password.setPlaceholderText(_translate("LoginForm", "Enter your password"))
        self.btn_login.setText(_translate("LoginForm", "LOG IN"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())