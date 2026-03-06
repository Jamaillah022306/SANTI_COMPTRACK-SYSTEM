# Responsive Admin Dashboard UI - Resizable
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QSizePolicy
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Ui_AdminDashboard(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("AdminDashboard")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(800, 500)
        MainWindow.setStyleSheet("background-color: rgb(236, 240, 241);")

        # Central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Main layout
        main_layout = QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ========== HEADER ==========
        self.frame_header = QtWidgets.QFrame()
        self.frame_header.setMinimumHeight(70)
        self.frame_header.setMaximumHeight(70)
        self.frame_header.setStyleSheet("QFrame { background-color: rgb(44, 62, 80); }")
        self.frame_header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)

        header_layout = QHBoxLayout(self.frame_header)
        header_layout.setContentsMargins(20, 10, 20, 10)
        header_layout.setSpacing(12)

        # Logo Image
        self.label_logo_image = QtWidgets.QLabel()
        self.label_logo_image.setFixedSize(70, 50)
        self.label_logo_image.setStyleSheet("background: white; margin: 2px; border-radius: 3px;")
        self.label_logo_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        logo_pixmap = QtGui.QPixmap(
            r"C:\Users\asus\PycharmProjects\Inventory_System_Final\SOURCE\logo.png"
        )
        if not logo_pixmap.isNull():
            self.label_logo_image.setPixmap(
                logo_pixmap.scaled(50, 50,
                                   QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                   QtCore.Qt.TransformationMode.SmoothTransformation)
            )
        header_layout.addWidget(self.label_logo_image)

        # System Title
        self.label_title = QtWidgets.QLabel()
        self.label_title.setStyleSheet(
            "color: white; font: bold 20pt 'Segoe UI'; background: transparent;"
        )
        header_layout.addWidget(self.label_title)

        header_layout.addStretch()

        # User Info
        self.label_user = QtWidgets.QLabel()
        self.label_user.setStyleSheet(
            "color: rgb(189, 195, 199); font: 11pt 'Segoe UI'; background: transparent;"
        )
        header_layout.addWidget(self.label_user)

        # Logout Button
        self.btn_logout = QtWidgets.QPushButton()
        self.btn_logout.setMinimumWidth(100)
        self.btn_logout.setMaximumWidth(120)
        self.btn_logout.setFixedHeight(38)
        self.btn_logout.setStyleSheet("""
            QPushButton {
                background-color: rgb(231, 76, 60);
                color: white;
                border: none;
                border-radius: 5px;
                font: bold 10pt 'Segoe UI';
            }
            QPushButton:hover { background-color: rgb(192, 57, 43); }
        """)
        header_layout.addWidget(self.btn_logout)

        main_layout.addWidget(self.frame_header)

        # ========== TAB WIDGET ==========
        tab_container = QtWidgets.QWidget()
        tab_container_layout = QVBoxLayout(tab_container)
        tab_container_layout.setContentsMargins(20, 20, 20, 20)

        self.tab_widget = QtWidgets.QTabWidget()
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

        self.create_dashboard_tab()
        self.create_history_tab()
        self.create_inventory_tab()

        self.tab_widget.setCurrentIndex(0)
        tab_container_layout.addWidget(self.tab_widget)
        main_layout.addWidget(tab_container)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_dashboard_tab(self):
        self.tab_dashboard = QtWidgets.QWidget()
        dash_layout = QVBoxLayout(self.tab_dashboard)
        dash_layout.setContentsMargins(30, 20, 30, 20)
        dash_layout.setSpacing(16)

        # Title
        self.label_dash_title = QtWidgets.QLabel()
        self.label_dash_title.setStyleSheet(
            "color: rgb(52, 73, 94); font: bold 18pt 'Segoe UI'; background: transparent;"
        )
        dash_layout.addWidget(self.label_dash_title)

        # Summary Cards
        cards_row = QHBoxLayout()
        cards_row.setSpacing(16)

        def make_card(bg_color, obj_title, obj_value):
            card = QtWidgets.QFrame()
            card.setMinimumHeight(100)
            card.setStyleSheet(
                "QFrame { background-color: " + bg_color + "; border-radius: 10px; }"
            )
            cl = QVBoxLayout(card)
            cl.setContentsMargins(20, 12, 20, 12)
            lbl_t = QtWidgets.QLabel()
            lbl_t.setStyleSheet("color: rgba(255,255,255,200); font: 10pt 'Segoe UI'; background: transparent;")
            lbl_v = QtWidgets.QLabel()
            lbl_v.setStyleSheet("color: white; font: bold 30pt 'Segoe UI'; background: transparent;")
            lbl_v.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
            cl.addWidget(lbl_t)
            cl.addWidget(lbl_v)
            setattr(self, obj_title, lbl_t)
            setattr(self, obj_value, lbl_v)
            return card

        cards_row.addWidget(make_card("rgb(52, 152, 219)",  "lbl_card_total_t",    "lbl_card_total_v"))
        cards_row.addWidget(make_card("rgb(231, 76, 60)",   "lbl_card_lowstock_t", "lbl_card_lowstock_v"))
        cards_row.addWidget(make_card("rgb(46, 204, 113)",  "lbl_card_stockin_t",  "lbl_card_stockin_v"))
        cards_row.addWidget(make_card("rgb(230, 126, 34)",  "lbl_card_stockout_t", "lbl_card_stockout_v"))
        dash_layout.addLayout(cards_row)

        # Charts Row
        charts_row = QHBoxLayout()
        charts_row.setSpacing(16)

        # Bar Chart
        bar_frame = QtWidgets.QFrame()
        bar_frame.setStyleSheet("QFrame { background: white; border-radius: 8px; }")
        bar_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        bar_fl = QVBoxLayout(bar_frame)
        bar_fl.setContentsMargins(10, 10, 10, 10)
        self.bar_label = QtWidgets.QLabel("Stock In vs Stock Out per Item")
        self.bar_label.setStyleSheet("color: rgb(52,73,94); font: bold 11pt 'Segoe UI';")
        bar_fl.addWidget(self.bar_label)
        self.bar_fig = Figure(figsize=(7, 4), facecolor='white')
        self.bar_canvas = FigureCanvas(self.bar_fig)
        self.bar_canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        bar_fl.addWidget(self.bar_canvas)
        charts_row.addWidget(bar_frame, stretch=3)

        # Pie Chart
        pie_frame = QtWidgets.QFrame()
        pie_frame.setStyleSheet("QFrame { background: white; border-radius: 8px; }")
        pie_frame.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        pie_fl = QVBoxLayout(pie_frame)
        pie_fl.setContentsMargins(10, 10, 10, 10)
        self.pie_label = QtWidgets.QLabel("Overall Stock In vs Out")
        self.pie_label.setStyleSheet("color: rgb(52,73,94); font: bold 11pt 'Segoe UI';")
        pie_fl.addWidget(self.pie_label)
        self.pie_fig = Figure(figsize=(4, 4), facecolor='white')
        self.pie_canvas = FigureCanvas(self.pie_fig)
        self.pie_canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        pie_fl.addWidget(self.pie_canvas)
        charts_row.addWidget(pie_frame, stretch=2)

        dash_layout.addLayout(charts_row)
        self.tab_widget.addTab(self.tab_dashboard, "")

    def create_history_tab(self):
        self.tab_history = QtWidgets.QWidget()
        history_layout = QVBoxLayout(self.tab_history)
        history_layout.setContentsMargins(30, 20, 30, 20)
        history_layout.setSpacing(20)

        # Top row
        top_row = QHBoxLayout()
        top_row.setSpacing(12)

        self.label_history_title = QtWidgets.QLabel()
        self.label_history_title.setStyleSheet(
            "color: rgb(52, 73, 94); font: bold 18pt 'Segoe UI'; background: transparent;"
        )
        top_row.addWidget(self.label_history_title)
        top_row.addStretch()

        self.label_date_from = QtWidgets.QLabel()
        self.label_date_from.setStyleSheet("color: rgb(52, 73, 94); font: 10pt 'Segoe UI';")
        top_row.addWidget(self.label_date_from)

        self.date_from = QtWidgets.QDateEdit()
        self.date_from.setDate(QtCore.QDate.currentDate())
        self.date_from.setMinimumWidth(140)
        self.date_from.setFixedHeight(35)
        self.date_from.setStyleSheet("color: black; padding: 5px;")
        self.date_from.setCalendarPopup(True)
        top_row.addWidget(self.date_from)

        self.label_date_to = QtWidgets.QLabel()
        self.label_date_to.setStyleSheet("color: rgb(52, 73, 94); font: 10pt 'Segoe UI';")
        top_row.addWidget(self.label_date_to)

        self.date_to = QtWidgets.QDateEdit()
        self.date_to.setDate(QtCore.QDate.currentDate())
        self.date_to.setMinimumWidth(140)
        self.date_to.setFixedHeight(35)
        self.date_to.setStyleSheet("color: black; padding: 5px;")
        self.date_to.setCalendarPopup(True)
        top_row.addWidget(self.date_to)

        self.btn_filter = QtWidgets.QPushButton()
        self.btn_filter.setFixedSize(70, 35)
        self.btn_filter.setStyleSheet("""
            QPushButton {
                background-color: rgb(142, 68, 173); color: white;
                border-radius: 5px; font: bold 10pt 'Segoe UI';
            }
            QPushButton:hover { background-color: rgb(120, 50, 150); }
        """)
        top_row.addWidget(self.btn_filter)

        self.btn_export = QtWidgets.QPushButton()
        self.btn_export.setFixedSize(95, 35)
        self.btn_export.setStyleSheet("""
            QPushButton {
                background-color: rgb(46, 204, 113); color: white;
                border-radius: 5px; font: bold 10pt 'Segoe UI';
            }
            QPushButton:hover { background-color: rgb(39, 174, 96); }
        """)
        top_row.addWidget(self.btn_export)

        history_layout.addLayout(top_row)

        # Table
        self.table_history = QtWidgets.QTableWidget()
        self.table_history.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_history.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.table_history.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid rgb(189, 195, 199);
                border-radius: 5px;
                gridline-color: rgb(236, 240, 241);
                color: black;
                text-align: center;
            }
            QHeaderView::section {
                background-color: rgb(52, 73, 94);
                color: white;
                padding: 8px;
                border: none;
                font: bold 10pt 'Segoe UI';
            }
        """)
        self.table_history.setColumnCount(7)
        self.table_history.setHorizontalHeaderLabels(
            ["Transaction ID", "Date & Time", "Item", "Type", "Quantity", "Stock", "User"]
        )
        self.table_history.setColumnWidth(0, 120)
        self.table_history.setColumnWidth(1, 170)
        self.table_history.setColumnWidth(2, 300)
        self.table_history.setColumnWidth(3, 130)
        self.table_history.setColumnWidth(4, 90)
        self.table_history.setColumnWidth(5, 90)
        self.table_history.horizontalHeader().setStretchLastSection(True)
        self.table_history.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Interactive
        )
        self.table_history.verticalHeader().setVisible(False)
        self.table_history.setSortingEnabled(True)

        history_layout.addWidget(self.table_history)
        self.tab_widget.addTab(self.tab_history, "")

    def create_inventory_tab(self):
        self.tab_inventory = QtWidgets.QWidget()
        inventory_layout = QVBoxLayout(self.tab_inventory)
        inventory_layout.setContentsMargins(30, 20, 30, 20)
        inventory_layout.setSpacing(20)

        top_row = QHBoxLayout()
        top_row.setSpacing(20)

        self.label_inventory_title = QtWidgets.QLabel()
        self.label_inventory_title.setStyleSheet(
            "color: rgb(52, 73, 94); font: bold 18pt 'Segoe UI'; background: transparent;"
        )
        top_row.addWidget(self.label_inventory_title)
        top_row.addStretch()

        self.search_inventory = QtWidgets.QLineEdit()
        self.search_inventory.setMinimumWidth(200)
        self.search_inventory.setMaximumWidth(300)
        self.search_inventory.setFixedHeight(35)
        self.search_inventory.setStyleSheet("""
            QLineEdit {
                border: 1px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding: 5px 10px;
                font: 10pt 'Segoe UI';
                color: black;
            }
        """)
        self.search_inventory.setPlaceholderText("Search items...")
        top_row.addWidget(self.search_inventory)

        inventory_layout.addLayout(top_row)

        self.table_inventory = QtWidgets.QTableWidget()
        self.table_inventory.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_inventory.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.table_inventory.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid rgb(189, 195, 199);
                border-radius: 5px;
                gridline-color: rgb(236, 240, 241);
                color: black;
                text-align: center;
            }
            QHeaderView::section {
                background-color: rgb(52, 73, 94);
                color: white;
                padding: 8px;
                border: none;
                font: bold 10pt 'Segoe UI';
            }
        """)
        self.table_inventory.setColumnCount(6)
        self.table_inventory.setHorizontalHeaderLabels(
            ["Item Name", "Category", "Current Stock", "Min Stock", "Price", "Status"]
        )
        self.table_inventory.setColumnWidth(0, 220)
        self.table_inventory.setColumnWidth(1, 180)
        self.table_inventory.setColumnWidth(2, 120)
        self.table_inventory.setColumnWidth(3, 100)
        self.table_inventory.setColumnWidth(4, 100)
        self.table_inventory.horizontalHeader().setStretchLastSection(True)
        self.table_inventory.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Interactive
        )
        self.table_inventory.verticalHeader().setVisible(False)
        self.table_inventory.setSortingEnabled(True)

        inventory_layout.addWidget(self.table_inventory)
        self.tab_widget.addTab(self.tab_inventory, "")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("AdminDashboard", "Inventory System - Admin Dashboard"))
        self.label_title.setText(_translate("AdminDashboard", "COMPUTER INVENTORY"))
        self.label_user.setText(_translate("AdminDashboard", "Logged in as: Administrator"))
        self.btn_logout.setText(_translate("AdminDashboard", "Logout"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_dashboard),
                                   _translate("AdminDashboard", "Dashboard"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_history),
                                   _translate("AdminDashboard", "View Reports"))
        self.label_dash_title.setText(_translate("AdminDashboard", "Analytics Overview"))
        self.lbl_card_total_t.setText(_translate("AdminDashboard", "Total Items"))
        self.lbl_card_total_v.setText(_translate("AdminDashboard", "0"))
        self.lbl_card_lowstock_t.setText(_translate("AdminDashboard", "Low Stock Alert"))
        self.lbl_card_lowstock_v.setText(_translate("AdminDashboard", "0"))
        self.lbl_card_stockin_t.setText(_translate("AdminDashboard", "Total Stock In"))
        self.lbl_card_stockin_v.setText(_translate("AdminDashboard", "0"))
        self.lbl_card_stockout_t.setText(_translate("AdminDashboard", "Total Stock Out"))
        self.lbl_card_stockout_v.setText(_translate("AdminDashboard", "0"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_inventory),
                                   _translate("AdminDashboard", "View Inventory"))
        self.label_history_title.setText(_translate("AdminDashboard", "Stock History"))
        self.label_date_from.setText(_translate("AdminDashboard", "From:"))
        self.label_date_to.setText(_translate("AdminDashboard", "To:"))
        self.btn_filter.setText(_translate("AdminDashboard", "Filter"))
        self.btn_export.setText(_translate("AdminDashboard", "📊 Export"))
        self.label_inventory_title.setText(_translate("AdminDashboard", "Current Inventory"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminDashboard()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())