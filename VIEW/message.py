from PyQt6.QtWidgets import QMessageBox

class Ui_message(object):
    def __init__(self):
        # Define a universal stylesheet for all message boxes
        # This forces a dark background with light text to ensure visibility
        self.msg_stylesheet = """
            QMessageBox {
                background-color: white;
            }
            QLabel {
                color: black;
                font-size: 13px;
            }
            QPushButton {
                background-color: #555555;
                color: white;
                border: 1px solid #777777;
                padding: 5px 15px;
                border-radius: 3px;
                min-width: 70px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
        """

    def apply_style(self, msg):
        """Helper to apply the stylesheet to any message box instance."""
        msg.setStyleSheet(self.msg_stylesheet)

    def show_warning(self, parent, title, message):
        msg = QMessageBox(parent)
        self.apply_style(msg) # Apply the fix
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def show_critical(self, parent, title, message):
        msg = QMessageBox(parent)
        self.apply_style(msg) # Apply the fix
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def confirmation(self, parent, title, message):
        msg = QMessageBox(parent)
        self.apply_style(msg) # Apply the fix
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        return msg.exec() == QMessageBox.StandardButton.Yes

    def show_information(self, parent, title, message):
        msg = QMessageBox(parent)
        self.apply_style(msg) # Apply the fix
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec()