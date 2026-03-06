import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from VIEW.login import Ui_LoginForm
from VIEW.message import Ui_message
from MODEL.database import db
from CONTROLLER.admin import admin
from CONTROLLER.staff import staff


# ===================== LOGIN WINDOW =====================
class Login(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.ui = Ui_LoginForm()
        self.mes = Ui_message()
        self.ui.setupUi(self)

        self.db = db()

        self.ui.input_username.returnPressed.connect(self.ui.input_password.setFocus)
        self.ui.input_password.returnPressed.connect(self.ui.btn_login.animateClick)
        self.ui.btn_login.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.input_username.text().strip()
        password = self.ui.input_password.text().strip()

        if not username or not password:
            self.mes.show_information(
                self, "Error", "Please enter both username and password"
            )
            return

        user = self.db.result(username, password)

        if not user:
            self.mes.show_warning(
                self, "Error", "Invalid username or password"
            )
            return

        role = user.get("role")

        if role not in ("Admin", "Staff"):
            self.mes.show_warning(
                self, "Error", "User role is invalid"
            )
            return

        fname = user.get("FullName")
        self.manager.user_session(fname)

        self.mes.show_information(
            self, "Success", "You have successfully logged in"
        )

        self.open_role_window(role)

    def open_role_window(self, role):
        if role == "Admin":
            self.manager.show_admin()
        elif role == "Staff":
            self.manager.show_staff()


# ===================== WINDOW MANAGER =====================
class Manager:
    def __init__(self):
        self.current_window = None
        self.fullname = ""
        self.show_login()

    def user_session(self, fullname):
        self.fullname = fullname

    def switch_window(self, window):
        if self.current_window:
            self.current_window.close()
        self.current_window = window
        self.current_window.show()

    def show_login(self):
        self.switch_window(Login(self))

    def show_admin(self):
        self.switch_window(admin(self, self.fullname))

    def show_staff(self):
        self.switch_window(staff(self, self.fullname))


# ===================== APP ENTRY =====================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec())