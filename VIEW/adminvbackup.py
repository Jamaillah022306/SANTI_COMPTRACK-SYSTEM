# Improved Admin Dashboard UI - Full Management Features
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_AdminDashboard(object):
    def setupUi(self, Form):
        Form.setObjectName("AdminDashboard")
        Form.resize(1280, 720)
        Form.setStyleSheet("background-color: rgb(236, 240, 241);")

        # ========== HEADER ==========
        self.frame_header = QtWidgets.QFrame(parent=Form)
        self.frame_header.setGeometry(QtCore.QRect(0, 0, 1280, 80))
        self.frame_header.setStyleSheet("""
            QFrame {
                background-color: rgb(44, 62, 80);
                border-bottom: 3px solid rgb(142, 68, 173);
            }
        """)
        self.frame_header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_header.setObjectName("frame_header")

        # System Title
        self.label_title = QtWidgets.QLabel(parent=self.frame_header)
        self.label_title.setGeometry(QtCore.QRect(30, 20, 450, 40))
        self.label_title.setStyleSheet("color: white; "
                                       "font: bold 20pt 'Segoe UI'; "
                                       "background: transparent;")
        self.label_title.setObjectName("label_title")

        # User Info
        self.label_user = QtWidgets.QLabel(parent=self.frame_header)
        self.label_user.setGeometry(QtCore.QRect(870, 25, 280, 30))
        self.label_user.setStyleSheet("color: rgb(189, 195, 199); "
                                      "font: 11pt 'Segoe UI'; "
                                      "background: transparent;")
        self.label_user.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.label_user.setObjectName("label_user")

        # Logout Button
        self.btn_logout = QtWidgets.QPushButton(parent=self.frame_header)
        self.btn_logout.setGeometry(QtCore.QRect(1160, 20, 100, 40))
        self.btn_logout.setStyleSheet("""
            QPushButton {
                background-color: rgb(231, 76, 60);
                color: white;
                border: none;
                border-radius: 5px;
                font: bold 10pt 'Segoe UI';
            }
            QPushButton:hover {
                background-color: rgb(192, 57, 43);
            }
        """)
        self.btn_logout.setObjectName("btn_logout")

        # ========== TAB WIDGET ==========
        self.tab_widget = QtWidgets.QTabWidget(parent=Form)
        self.tab_widget.setGeometry(QtCore.QRect(20, 100, 1240, 600))
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                background-color: white;
            }
            QTabBar::tab {
                background-color: rgb(189, 195, 199);
                color: rgb(52, 73, 94);
                padding: 12px 25px;
                margin-right: 2px;
                font: bold 10pt 'Segoe UI';
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
            }
            QTabBar::tab:selected {
                background-color: rgb(142, 68, 173);
                color: white;
            }
            QTabBar::tab:hover:!selected {
                background-color: rgb(149, 165, 166);
            }
        """)
        self.tab_widget.setObjectName("tab_widget")

        # ===== TAB 1: DASHBOARD =====
        self.create_dashboard_tab()

        # ===== TAB 3: MANAGE ITEMS =====
        self.create_manage_tab()

        # ===== TAB 4: TRANSACTION HISTORY =====
        self.create_history_tab()

        self.tab_widget.setCurrentIndex(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def create_dashboard_tab(self):
        self.tab_dashboard = QtWidgets.QWidget()
        self.tab_dashboard.setObjectName("tab_dashboard")

        # Summary Cards
        self.create_summary_cards(self.tab_dashboard)

        # Recent Activity
        self.label_recent = QtWidgets.QLabel(parent=self.tab_dashboard)
        self.label_recent.setGeometry(QtCore.QRect(30, 160, 200, 30))
        self.label_recent.setStyleSheet("color: rgb(52, 73, 94); "
                                        "font: bold 14pt 'Segoe UI'; background: transparent;")

        self.table_recent = QtWidgets.QTableWidget(parent=self.tab_dashboard)
        self.table_recent.setGeometry(QtCore.QRect(30, 200, 1180, 350))
        self.table_recent.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid rgb(189, 195, 199);
                border-radius: 5px;
                gridline-color: rgb(236, 240, 241);
                color: black;
            }
            QHeaderView::section {
                background-color: rgb(44, 62, 80);
                color: white;
                padding: 8px;
                border: none;
                font: bold 10pt 'Segoe UI';
            }
        """)
        self.table_recent.setColumnCount(6)
        self.table_recent.setHorizontalHeaderLabels(
            ["Date & Time", "Item Name", "Type", "Quantity", "Performed By", "Notes"]
        )
        self.table_recent.horizontalHeader().setStretchLastSection(True)
        self.table_recent.setColumnWidth(0, 180)
        self.table_recent.setColumnWidth(1, 250)
        self.table_recent.setColumnWidth(2, 100)
        self.table_recent.setColumnWidth(3, 100)
        self.table_recent.setColumnWidth(4, 150)
        self.table_recent.verticalHeader().setVisible(False)
        self.table_recent.setAlternatingRowColors(True)

        self.tab_widget.addTab(self.tab_dashboard, "")

    def create_summary_cards(self, parent):
        self.frame_summary = QtWidgets.QFrame(parent=parent)
        self.frame_summary.setGeometry(QtCore.QRect(30, 20, 1180, 120))
        self.frame_summary.setStyleSheet("background: transparent;")

        cards = [
            ("card_total", "label_total_title", "label_total_value", 0, "rgb(142, 68, 173)"),
            ("card_lowstock", "label_lowstock_title", "label_lowstock_value", 300, "rgb(231, 76, 60)"),
            ("card_stockin", "label_stockin_title", "label_stockin_value", 600, "rgb(46, 204, 113)"),
            ("card_stockout", "label_stockout_title", "label_stockout_value", 900, "rgb(230, 126, 34)")
        ]

        for card_name, title_name, value_name, x_pos, color in cards:
            card = QtWidgets.QFrame(parent=self.frame_summary)
            card.setGeometry(QtCore.QRect(x_pos, 0, 280, 110))
            card.setStyleSheet(f"QFrame {{ background-color: {color}; border-radius: 10px; }}")
            setattr(self, card_name, card)

            title = QtWidgets.QLabel(parent=card)
            title.setGeometry(QtCore.QRect(20, 15, 240, 25))
            title.setStyleSheet("color: rgba(255, 255, 255, 200); "
                                "font: 10pt 'Segoe UI'; background: transparent;")
            setattr(self, title_name, title)

            value = QtWidgets.QLabel(parent=card)
            value.setGeometry(QtCore.QRect(20, 45, 240, 50))
            value.setStyleSheet("color: white; "
                                "font: bold 32pt 'Segoe UI'; background: transparent;")
            setattr(self, value_name, value)

    def create_manage_tab(self):
        self.tab_manage = QtWidgets.QWidget()
        self.tab_manage.setObjectName("tab_manage")

        self.label_manage_title = QtWidgets.QLabel(parent=self.tab_manage)
        self.label_manage_title.setGeometry(QtCore.QRect(30, 20, 300, 35))
        self.label_manage_title.setStyleSheet(
            "color: rgb(52, 73, 94); font: bold 18pt 'Segoe UI'; background: transparent;")

        self.input_manage_search = QtWidgets.QLineEdit(parent=self.tab_manage)
        self.input_manage_search.setGeometry(QtCore.QRect(880, 20, 330, 40))
        self.input_manage_search.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color:black;
            }
        """)

        self.table_manage = QtWidgets.QTableWidget(parent=self.tab_manage)
        self.table_manage.setGeometry(QtCore.QRect(30, 80, 1180, 470))
        self.table_manage.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid rgb(189, 195, 199);
                border-radius: 5px;
                color: black;
            }
            QHeaderView::section {
                background-color: rgb(44, 62, 80);
                color: white;
                padding: 8px;
                font: bold 10pt 'Segoe UI';
            }
        """)
        self.table_manage.setColumnCount(6)
        self.table_manage.setHorizontalHeaderLabels(
            ["Item Name", "Category", "Stock", "Min Stock", "Price", "Status"]
        )
        self.table_manage.horizontalHeader().setStretchLastSection(True)
        self.table_manage.setColumnWidth(0, 280)
        self.table_manage.setColumnWidth(1, 180)
        self.table_manage.setColumnWidth(2, 100)
        self.table_manage.setColumnWidth(3, 100)
        self.table_manage.setColumnWidth(4, 120)
        self.table_manage.setColumnWidth(5, 120)
        self.table_manage.verticalHeader().setVisible(False)
        self.table_manage.setAlternatingRowColors(True)

        self.tab_widget.addTab(self.tab_manage, "")

    def create_history_tab(self):
        self.tab_history = QtWidgets.QWidget()
        self.tab_history.setObjectName("tab_history")

        self.label_history_title = QtWidgets.QLabel(parent=self.tab_history)
        self.label_history_title.setGeometry(QtCore.QRect(30, 20, 300, 35))
        self.label_history_title.setStyleSheet(
            "color: rgb(52, 73, 94); font: bold 18pt 'Segoe UI'; background: transparent;")

        # Date Filters
        self.label_date_from = QtWidgets.QLabel(parent=self.tab_history)
        self.label_date_from.setGeometry(QtCore.QRect(680, 25, 80, 30))
        self.label_date_from.setStyleSheet("color: rgb(52, 73, 94); font: 10pt 'Segoe UI';")

        self.date_from = QtWidgets.QDateEdit(parent=self.tab_history)
        self.date_from.setGeometry(QtCore.QRect(760, 20, 150, 35))
        self.date_from.setStyleSheet("color: black;")
        self.date_from.setCalendarPopup(True)

        self.label_date_to = QtWidgets.QLabel(parent=self.tab_history)
        self.label_date_to.setGeometry(QtCore.QRect(930, 25, 40, 30))
        self.label_date_to.setStyleSheet("color: rgb(52, 73, 94); font: 10pt 'Segoe UI';")

        self.date_to = QtWidgets.QDateEdit(parent=self.tab_history)
        self.date_to.setGeometry(QtCore.QRect(970, 20, 150, 35))
        self.date_to.setStyleSheet("color: black;")
        self.date_to.setCalendarPopup(True)

        self.btn_filter = QtWidgets.QPushButton(parent=self.tab_history)
        self.btn_filter.setGeometry(QtCore.QRect(1140, 20, 70, 35))
        self.btn_filter.setStyleSheet("""
            QPushButton {
                background-color: rgb(142, 68, 173);
                color: white;
                border-radius: 5px;
                font: bold 10pt 'Segoe UI';
            }
        """)

        self.table_history = QtWidgets.QTableWidget(parent=self.tab_history)
        self.table_history.setGeometry(QtCore.QRect(30, 80, 1180, 470))
        self.table_history.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid rgb(189, 195, 199);
                border-radius: 5px;
                color: black;
            }
            QHeaderView::section {
                background-color: rgb(44, 62, 80);
                color: white;
                padding: 8px;
                font: bold 10pt 'Segoe UI';
            }
        """)
        self.table_history.setColumnCount(7)
        self.table_history.setHorizontalHeaderLabels(
            ["Transaction ID", "Date & Time", "Item", "Type", "Quantity", "User", "Notes"]
        )
        self.table_history.setColumnWidth(0, 130)
        self.table_history.setColumnWidth(1, 150)
        self.table_history.setColumnWidth(2, 230)
        self.table_history.setColumnWidth(3, 120)
        self.table_history.setColumnWidth(4, 100)
        self.table_history.setColumnWidth(5, 200)
        self.table_history.setColumnWidth(6, 200)
        self.table_history.horizontalHeader().setStretchLastSection(True)
        self.table_history.verticalHeader().setVisible(False)
        self.table_history.setAlternatingRowColors(True)

        self.tab_widget.addTab(self.tab_history, "")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("AdminDashboard", "Inventory System - Admin Dashboard"))

        self.label_title.setText(_translate("AdminDashboard", "Admin - Computer Parts Inventory"))
        self.label_user.setText(_translate("AdminDashboard", "Logged in as: Administrator"))
        self.btn_logout.setText(_translate("AdminDashboard", "Logout"))

        # Tabs
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_dashboard),
                                   _translate("AdminDashboard", "Dashboard"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_manage),
                                   _translate("AdminDashboard", "View Items"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_history),
                                   _translate("AdminDashboard", "Transaction History"))

        # Dashboard Cards
        self.label_total_title.setText(_translate("AdminDashboard", "Total Items"))
        self.label_total_value.setText(_translate("AdminDashboard", "0"))
        self.label_lowstock_title.setText(_translate("AdminDashboard", "Low Stock Alert"))
        self.label_lowstock_value.setText(_translate("AdminDashboard", "0"))
        self.label_stockin_title.setText(_translate("AdminDashboard", "Stock In (Today)"))
        self.label_stockin_value.setText(_translate("AdminDashboard", "0"))
        self.label_stockout_title.setText(_translate("AdminDashboard", "Stock Out (Today)"))
        self.label_stockout_value.setText(_translate("AdminDashboard", "0"))
        self.label_recent.setText(_translate("AdminDashboard", "Recent Transactions"))
        # Manage
        self.label_manage_title.setText(_translate("AdminDashboard", "Manage Inventory"))
        self.input_manage_search.setPlaceholderText(_translate("AdminDashboard", "Search..."))
        # History
        self.label_history_title.setText(_translate("AdminDashboard", "Transaction History"))
        self.label_date_from.setText(_translate("AdminDashboard", "From:"))
        self.label_date_to.setText(_translate("AdminDashboard", "To:"))
        self.btn_filter.setText(_translate("AdminDashboard", "Filter"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_AdminDashboard()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())