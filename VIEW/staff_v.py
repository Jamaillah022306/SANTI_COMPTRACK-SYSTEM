# Improved Staff Dashboard UI - Stock In/Out Focus
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StaffDashboard(object):
    def setupUi(self, Form):
        Form.setObjectName("StaffDashboard")
        Form.resize(1280, 720)

        # ── Support both QMainWindow (controller) and QWidget (standalone test) ──
        if isinstance(Form, QtWidgets.QMainWindow):
            self.centralwidget = QtWidgets.QWidget(Form)
            self.centralwidget.setStyleSheet("background-color: rgb(236, 240, 241);")
            Form.setCentralWidget(self.centralwidget)
            container = self.centralwidget
        else:
            Form.setStyleSheet("background-color: rgb(236, 240, 241);")
            container = Form

        # ========== HEADER ==========
        self.frame_header = QtWidgets.QFrame(parent=container)
        self.frame_header.setGeometry(QtCore.QRect(0, 0, 1280, 80))
        self.frame_header.setStyleSheet("""
            QFrame {
                background-color: rgb(52, 73, 94);
            }
        """)
        self.frame_header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_header.setObjectName("frame_header")

        # Logo Image (left of title)
        self.label_logo_image = QtWidgets.QLabel(parent=self.frame_header)
        self.label_logo_image.setGeometry(QtCore.QRect(20, 15, 70, 50))
        self.label_logo_image.setStyleSheet("background: white; margin: 2px; border-radius: 3px;")
        self.label_logo_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_logo_image.setObjectName("label_logo_image")
        logo_pixmap = QtGui.QPixmap(r"C:\Users\asus\PycharmProjects\Inventory_System_Final\SOURCE\logo.png")
        if not logo_pixmap.isNull():
            self.label_logo_image.setPixmap(
                logo_pixmap.scaled(50, 50,
                                   QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                   QtCore.Qt.TransformationMode.SmoothTransformation)
            )

        # System Title
        self.label_title = QtWidgets.QLabel(parent=self.frame_header)
        self.label_title.setGeometry(QtCore.QRect(100, 20, 400, 40))
        self.label_title.setStyleSheet("color: white; "
                                       "font: bold 20pt 'Segoe UI'; "
                                       "background: transparent;")
        self.label_title.setObjectName("label_title")

        # User Info
        self.label_user = QtWidgets.QLabel(parent=self.frame_header)
        self.label_user.setGeometry(QtCore.QRect(900, 25, 250, 30))
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
        self.tab_widget = QtWidgets.QTabWidget(parent=container)
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
                padding: 12px 30px;
                margin-right: 2px;
                font: bold 11pt 'Segoe UI';
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
            }
            QTabBar::tab:selected {
                background-color: rgb(52, 152, 219);
                color: white;
            }
            QTabBar::tab:hover:!selected {
                background-color: rgb(149, 165, 166);
            }
        """)
        self.tab_widget.setObjectName("tab_widget")

        # ===========================
        # TAB 1: DASHBOARD / OVERVIEW
        # ===========================
        self.tab_dashboard = QtWidgets.QWidget()
        self.tab_dashboard.setObjectName("tab_dashboard")

        # Summary Cards Frame
        self.frame_summary = QtWidgets.QFrame(parent=self.tab_dashboard)
        self.frame_summary.setGeometry(QtCore.QRect(30, 20, 1180, 120))
        self.frame_summary.setStyleSheet("background: transparent;")
        self.frame_summary.setObjectName("frame_summary")

        # Card 1: Total Items
        self.card_total = QtWidgets.QFrame(parent=self.frame_summary)
        self.card_total.setGeometry(QtCore.QRect(0, 0, 280, 110))
        self.card_total.setStyleSheet("""
            QFrame {
                background-color: rgb(52, 152, 219);
                border-radius: 10px;
            }
        """)
        self.card_total.setObjectName("card_total")

        self.label_total_title = QtWidgets.QLabel(parent=self.card_total)
        self.label_total_title.setGeometry(QtCore.QRect(20, 15, 240, 25))
        self.label_total_title.setStyleSheet("color: rgba(255, 255, 255, 200); "
                                             "font: 10pt 'Segoe UI'; "
                                             "background: transparent;")
        self.label_total_title.setObjectName("label_total_title")

        self.label_total_value = QtWidgets.QLabel(parent=self.card_total)
        self.label_total_value.setGeometry(QtCore.QRect(20, 45, 240, 50))
        self.label_total_value.setStyleSheet("color: white; "
                                             "font: bold 32pt 'Segoe UI'; "
                                             "background: transparent;")
        self.label_total_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_total_value.setObjectName("label_total_value")

        # Card 2: Low Stock Items
        self.card_lowstock = QtWidgets.QFrame(parent=self.frame_summary)
        self.card_lowstock.setGeometry(QtCore.QRect(300, 0, 280, 110))
        self.card_lowstock.setStyleSheet("""
            QFrame {
                background-color: rgb(231, 76, 60);
                border-radius: 10px;
            }
        """)
        self.card_lowstock.setObjectName("card_lowstock")

        self.label_lowstock_title = QtWidgets.QLabel(parent=self.card_lowstock)
        self.label_lowstock_title.setGeometry(QtCore.QRect(20, 15, 240, 25))
        self.label_lowstock_title.setStyleSheet("color: rgba(255, 255, 255, 200); "
                                                "font: 10pt 'Segoe UI'; "
                                                "background: transparent;")
        self.label_lowstock_title.setObjectName("label_lowstock_title")

        self.label_lowstock_value = QtWidgets.QLabel(parent=self.card_lowstock)
        self.label_lowstock_value.setGeometry(QtCore.QRect(20, 45, 240, 50))
        self.label_lowstock_value.setStyleSheet("color: white; "
                                                "font: bold 32pt 'Segoe UI'; "
                                                "background: transparent;")
        self.label_lowstock_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_lowstock_value.setObjectName("label_lowstock_value")

        # Card 3: Stock In (Today)
        self.card_stockin = QtWidgets.QFrame(parent=self.frame_summary)
        self.card_stockin.setGeometry(QtCore.QRect(600, 0, 280, 110))
        self.card_stockin.setStyleSheet("""
            QFrame {
                background-color: rgb(46, 204, 113);
                border-radius: 10px;
            }
        """)
        self.card_stockin.setObjectName("card_stockin")

        self.label_stockin_title = QtWidgets.QLabel(parent=self.card_stockin)
        self.label_stockin_title.setGeometry(QtCore.QRect(20, 15, 240, 25))
        self.label_stockin_title.setStyleSheet("color: rgba(255, 255, 255, 200); "
                                               "font: 10pt 'Segoe UI'; "
                                               "background: transparent;")
        self.label_stockin_title.setObjectName("label_stockin_title")

        self.label_stockin_value = QtWidgets.QLabel(parent=self.card_stockin)
        self.label_stockin_value.setGeometry(QtCore.QRect(20, 45, 240, 50))
        self.label_stockin_value.setStyleSheet("color: white; "
                                               "font: bold 32pt 'Segoe UI'; "
                                               "background: transparent;")
        self.label_stockin_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_stockin_value.setObjectName("label_stockin_value")

        # Card 4: Stock Out (Today)
        self.card_stockout = QtWidgets.QFrame(parent=self.frame_summary)
        self.card_stockout.setGeometry(QtCore.QRect(900, 0, 280, 110))
        self.card_stockout.setStyleSheet("""
            QFrame {
                background-color: rgb(230, 126, 34);
                border-radius: 10px;
            }
        """)
        self.card_stockout.setObjectName("card_stockout")

        self.label_stockout_title = QtWidgets.QLabel(parent=self.card_stockout)
        self.label_stockout_title.setGeometry(QtCore.QRect(20, 15, 240, 25))
        self.label_stockout_title.setStyleSheet("color: rgba(255, 255, 255, 200); "
                                                "font: 10pt 'Segoe UI'; "
                                                "background: transparent;")
        self.label_stockout_title.setObjectName("label_stockout_title")

        self.label_stockout_value = QtWidgets.QLabel(parent=self.card_stockout)
        self.label_stockout_value.setGeometry(QtCore.QRect(20, 45, 240, 50))
        self.label_stockout_value.setStyleSheet("color: white; "
                                                "font: bold 32pt 'Segoe UI'; "
                                                "background: transparent;")
        self.label_stockout_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_stockout_value.setObjectName("label_stockout_value")

        # Recent Activity Table
        self.label_recent = QtWidgets.QLabel(parent=self.tab_dashboard)
        self.label_recent.setGeometry(QtCore.QRect(30, 160, 200, 30))
        self.label_recent.setStyleSheet("color: rgb(52, 73, 94); "
                                        "font: bold 14pt 'Segoe UI'; "
                                        "background: transparent;")
        self.label_recent.setObjectName("label_recent")

        self.table_recent = QtWidgets.QTableWidget(parent=self.tab_dashboard)
        self.table_recent.setGeometry(QtCore.QRect(30, 200, 1180, 350))
        self.table_recent.setStyleSheet("""
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
        self.table_recent.setColumnCount(6)
        self.table_recent.setRowCount(0)
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
        self.table_recent.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_recent.setObjectName("table_recent")

        self.tab_widget.addTab(self.tab_dashboard, "")

        # ===========================
        # TAB 2: ADD NEW ITEM
        # ===========================
        self.tab_additem = QtWidgets.QWidget()
        self.tab_additem.setObjectName("tab_additem")

        # Title
        self.label_additem_page = QtWidgets.QLabel(parent=self.tab_additem)
        self.label_additem_page.setGeometry(QtCore.QRect(30, 20, 300, 35))
        self.label_additem_page.setStyleSheet("color: rgb(52, 73, 94); "
                                              "font: bold 18pt 'Segoe UI'; "
                                              "background: transparent;")
        self.label_additem_page.setObjectName("label_additem_page")

        # Form Container
        self.frame_additem_form = QtWidgets.QFrame(parent=self.tab_additem)
        self.frame_additem_form.setGeometry(QtCore.QRect(30, 80, 1180, 470))
        self.frame_additem_form.setStyleSheet("""
            QFrame {
                background-color: rgb(250, 251, 252);
                border: 2px solid rgb(189, 195, 199);
                border-radius: 10px;
            }
            QLabel { border: none; background: transparent; }
        """)
        self.frame_additem_form.setObjectName("frame_additem_form")

        # Item Name
        self.label_additem_name = QtWidgets.QLabel(parent=self.frame_additem_form)
        self.label_additem_name.setGeometry(QtCore.QRect(40, 40, 150, 25))
        self.label_additem_name.setStyleSheet("color: rgb(52, 73, 94); "
                                              "font: bold 11pt 'Segoe UI'; "
                                              "background: transparent;")
        self.label_additem_name.setObjectName("label_additem_name")

        self.input_additem_name = QtWidgets.QLineEdit(parent=self.frame_additem_form)
        self.input_additem_name.setGeometry(QtCore.QRect(40, 70, 1100, 45))
        self.input_additem_name.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QLineEdit:focus {
                border: 2px solid rgb(52, 152, 219);
            }
        """)
        self.input_additem_name.setObjectName("input_additem_name")

        # Category
        self.label_additem_category = QtWidgets.QLabel(parent=self.frame_additem_form)
        self.label_additem_category.setGeometry(QtCore.QRect(40, 140, 150, 25))
        self.label_additem_category.setStyleSheet("color: rgb(52, 73, 94); "
                                                  "font: bold 11pt 'Segoe UI'; "
                                                  "background: transparent;")
        self.label_additem_category.setObjectName("label_additem_category")

        self.combo_additem_category = QtWidgets.QComboBox(parent=self.frame_additem_form)
        self.combo_additem_category.setGeometry(QtCore.QRect(40, 170, 1100, 45))
        self.combo_additem_category.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QComboBox:focus {
                border: 2px solid rgb(52, 152, 219);
            }
            QComboBox::drop-down {
                border: none;
                width: 30px;
                color: black;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                selection-background-color: rgb(52, 152, 219);
                selection-color: white;
            }
        """)
        self.combo_additem_category.addItem("Select Category")
        self.combo_additem_category.addItem("CPU (Processor)")
        self.combo_additem_category.addItem("GPU (Graphics Card)")
        self.combo_additem_category.addItem("RAM (Memory)")
        self.combo_additem_category.addItem("Storage (SSD/HDD)")
        self.combo_additem_category.addItem("Motherboard")
        self.combo_additem_category.addItem("Power Supply")
        self.combo_additem_category.addItem("Case/Chassis")
        self.combo_additem_category.addItem("Cooling")
        self.combo_additem_category.addItem("Peripherals")
        self.combo_additem_category.addItem("Accessories")
        self.combo_additem_category.addItem("Other")
        self.combo_additem_category.setObjectName("combo_additem_category")

        # Initial Stock
        self.label_additem_stock = QtWidgets.QLabel(parent=self.frame_additem_form)
        self.label_additem_stock.setGeometry(QtCore.QRect(40, 240, 150, 25))
        self.label_additem_stock.setStyleSheet("color: rgb(52, 73, 94); "
                                               "font: bold 11pt 'Segoe UI'; "
                                               "background: transparent;")
        self.label_additem_stock.setObjectName("label_additem_stock")

        self.input_additem_stock = QtWidgets.QLineEdit(parent=self.frame_additem_form)
        self.input_additem_stock.setGeometry(QtCore.QRect(40, 270, 340, 45))
        self.input_additem_stock.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QLineEdit:focus {
                border: 2px solid rgb(52, 152, 219);
            }
        """)
        self.input_additem_stock.setObjectName("input_additem_stock")

        # Min Stock
        self.label_additem_minstock = QtWidgets.QLabel(parent=self.frame_additem_form)
        self.label_additem_minstock.setGeometry(QtCore.QRect(420, 240, 150, 25))
        self.label_additem_minstock.setStyleSheet("color: rgb(52, 73, 94); "
                                                  "font: bold 11pt 'Segoe UI'; "
                                                  "background: transparent;")
        self.label_additem_minstock.setObjectName("label_additem_minstock")

        self.input_additem_minstock = QtWidgets.QLineEdit(parent=self.frame_additem_form)
        self.input_additem_minstock.setGeometry(QtCore.QRect(420, 270, 340, 45))
        self.input_additem_minstock.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QLineEdit:focus {
                border: 2px solid rgb(52, 152, 219);
            }
        """)
        self.input_additem_minstock.setObjectName("input_additem_minstock")

        # Price
        self.label_additem_price = QtWidgets.QLabel(parent=self.frame_additem_form)
        self.label_additem_price.setGeometry(QtCore.QRect(800, 240, 150, 25))
        self.label_additem_price.setStyleSheet("color: rgb(52, 73, 94); "
                                               "font: bold 11pt 'Segoe UI'; "
                                               "background: transparent;")
        self.label_additem_price.setObjectName("label_additem_price")

        self.input_additem_price = QtWidgets.QLineEdit(parent=self.frame_additem_form)
        self.input_additem_price.setGeometry(QtCore.QRect(800, 270, 340, 45))
        self.input_additem_price.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QLineEdit:focus {
                border: 2px solid rgb(52, 152, 219);
            }
        """)
        self.input_additem_price.setObjectName("input_additem_price")

        # Add Item Button
        self.btn_add_newitem = QtWidgets.QPushButton(parent=self.frame_additem_form)
        self.btn_add_newitem.setGeometry(QtCore.QRect(40, 395, 1100, 55))
        self.btn_add_newitem.setStyleSheet("""
            QPushButton {
                background-color: rgb(52, 152, 219);
                color: white;
                border: none;
                border-radius: 5px;
                font: bold 13pt 'Segoe UI';
            }
            QPushButton:hover {
                background-color: rgb(41, 128, 185);
            }
            QPushButton:pressed {
                background-color: rgb(31, 97, 141);
            }
        """)
        self.btn_add_newitem.setObjectName("btn_add_newitem")

        self.tab_widget.addTab(self.tab_additem, "")

        # ===========================
        # TAB 3: STOCK IN
        # ===========================
        self.tab_stockin = QtWidgets.QWidget()
        self.tab_stockin.setObjectName("tab_stockin")

        self.label_stockin_page = QtWidgets.QLabel(parent=self.tab_stockin)
        self.label_stockin_page.setGeometry(QtCore.QRect(30, 20, 300, 35))
        self.label_stockin_page.setStyleSheet(
            "color: rgb(52, 73, 94); font: bold 18pt 'Segoe UI'; background: transparent;"
        )
        self.label_stockin_page.setObjectName("label_stockin_page")

        self.frame_stockin_form = QtWidgets.QFrame(parent=self.tab_stockin)
        self.frame_stockin_form.setGeometry(QtCore.QRect(30, 80, 1180, 470))
        self.frame_stockin_form.setStyleSheet("""
            QFrame {
                background-color: rgb(250, 251, 252);
                border: 2px solid rgb(189, 195, 199);
                border-radius: 10px;
            }
            QLabel { border: none; background: transparent; }
        """)
        self.frame_stockin_form.setObjectName("frame_stockin_form")

        self.label_stockin_item = QtWidgets.QLabel(parent=self.frame_stockin_form)
        self.label_stockin_item.setGeometry(QtCore.QRect(40, 40, 200, 25))
        self.label_stockin_item.setStyleSheet(
            "color: rgb(52, 73, 94); font: bold 11pt 'Segoe UI'; background: transparent;"
        )
        self.label_stockin_item.setObjectName("label_stockin_item")

        self.combo_stockin_item = QtWidgets.QComboBox(parent=self.frame_stockin_form)
        self.combo_stockin_item.setGeometry(QtCore.QRect(40, 70, 530, 45))
        self.combo_stockin_item.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QComboBox:focus { border: 2px solid rgb(52, 152, 219); }
            QComboBox::drop-down { border: none; width: 30px; }
            QComboBox QAbstractItemView {
                background-color: white; color: black;
                selection-background-color: rgb(52, 152, 219);
                selection-color: white;
            }
        """)
        self.combo_stockin_item.setObjectName("combo_stockin_item")

        self.label_stockin_qty = QtWidgets.QLabel(parent=self.frame_stockin_form)
        self.label_stockin_qty.setGeometry(QtCore.QRect(610, 40, 150, 25))
        self.label_stockin_qty.setStyleSheet(
            "color: rgb(52, 73, 94); font: bold 11pt 'Segoe UI'; background: transparent;"
        )
        self.label_stockin_qty.setObjectName("label_stockin_qty")

        self.input_stockin_qty = QtWidgets.QLineEdit(parent=self.frame_stockin_form)
        self.input_stockin_qty.setGeometry(QtCore.QRect(610, 70, 530, 45))
        self.input_stockin_qty.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QLineEdit:focus { border: 2px solid rgb(52, 152, 219); }
        """)
        self.input_stockin_qty.setObjectName("input_stockin_qty")

        self.label_stockin_notes = QtWidgets.QLabel(parent=self.frame_stockin_form)
        self.label_stockin_notes.setGeometry(QtCore.QRect(40, 140, 200, 25))
        self.label_stockin_notes.setStyleSheet(
            "color: rgb(52, 73, 94); font: bold 11pt 'Segoe UI'; background: transparent;"
        )
        self.label_stockin_notes.setObjectName("label_stockin_notes")

        self.input_stockin_notes = QtWidgets.QTextEdit(parent=self.frame_stockin_form)
        self.input_stockin_notes.setGeometry(QtCore.QRect(40, 170, 1100, 100))
        self.input_stockin_notes.setStyleSheet("""
            QTextEdit {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding: 10px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QTextEdit:focus { border: 2px solid rgb(52, 152, 219); }
        """)
        self.input_stockin_notes.setObjectName("input_stockin_notes")

        self.btn_record_stockin = QtWidgets.QPushButton(parent=self.frame_stockin_form)
        self.btn_record_stockin.setGeometry(QtCore.QRect(40, 395, 1100, 55))
        self.btn_record_stockin.setStyleSheet("""
            QPushButton {
                background-color: rgb(46, 204, 113);
                color: white;
                border: none;
                border-radius: 5px;
                font: bold 13pt 'Segoe UI';
            }
            QPushButton:hover { background-color: rgb(39, 174, 96); }
            QPushButton:pressed { background-color: rgb(34, 153, 84); }
        """)
        self.btn_record_stockin.setObjectName("btn_record_stockin")

        self.tab_widget.addTab(self.tab_stockin, "")

        # ===========================
        # TAB 4: STOCK OUT
        # ===========================
        self.tab_stockout = QtWidgets.QWidget()
        self.tab_stockout.setObjectName("tab_stockout")

        self.label_stockout_page = QtWidgets.QLabel(parent=self.tab_stockout)
        self.label_stockout_page.setGeometry(QtCore.QRect(30, 20, 300, 35))
        self.label_stockout_page.setStyleSheet("color: rgb(52, 73, 94); "
                                               "font: bold 18pt 'Segoe UI'; "
                                               "background: transparent;")
        self.label_stockout_page.setObjectName("label_stockout_page")

        self.frame_stockout_form = QtWidgets.QFrame(parent=self.tab_stockout)
        self.frame_stockout_form.setGeometry(QtCore.QRect(30, 80, 1180, 470))
        self.frame_stockout_form.setStyleSheet("""
            QFrame {
                background-color: rgb(250, 251, 252);
                border: 2px solid rgb(189, 195, 199);
                border-radius: 10px;
            }
            QLabel { border: none; background: transparent; }
        """)
        self.frame_stockout_form.setObjectName("frame_stockout_form")

        self.label_stockout_item = QtWidgets.QLabel(parent=self.frame_stockout_form)
        self.label_stockout_item.setGeometry(QtCore.QRect(40, 40, 150, 25))
        self.label_stockout_item.setStyleSheet("color: rgb(52, 73, 94); "
                                               "font: bold 11pt 'Segoe UI'; "
                                               "background: transparent;")
        self.label_stockout_item.setObjectName("label_stockout_item")

        self.combo_stockout_item = QtWidgets.QComboBox(parent=self.frame_stockout_form)
        self.combo_stockout_item.setGeometry(QtCore.QRect(40, 70, 1100, 45))
        self.combo_stockout_item.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QComboBox:focus { border: 2px solid rgb(52, 152, 219); }
            QComboBox::drop-down { border: none; width: 30px; }
            QComboBox QAbstractItemView {
                background-color: white; color: black;
                selection-background-color: rgb(52, 152, 219);
                selection-color: white;
            }
        """)
        self.combo_stockout_item.setObjectName("combo_stockout_item")

        self.label_stockout_qty = QtWidgets.QLabel(parent=self.frame_stockout_form)
        self.label_stockout_qty.setGeometry(QtCore.QRect(40, 140, 150, 25))
        self.label_stockout_qty.setStyleSheet("color: rgb(52, 73, 94); "
                                              "font: bold 11pt 'Segoe UI'; "
                                              "background: transparent;")
        self.label_stockout_qty.setObjectName("label_stockout_qty")

        self.input_stockout_qty = QtWidgets.QLineEdit(parent=self.frame_stockout_form)
        self.input_stockout_qty.setGeometry(QtCore.QRect(40, 170, 530, 45))
        self.input_stockout_qty.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QLineEdit:focus { border: 2px solid rgb(52, 152, 219); }
        """)
        self.input_stockout_qty.setObjectName("input_stockout_qty")

        self.label_stockout_reason = QtWidgets.QLabel(parent=self.frame_stockout_form)
        self.label_stockout_reason.setGeometry(QtCore.QRect(610, 140, 150, 25))
        self.label_stockout_reason.setStyleSheet("color: rgb(52, 73, 94); "
                                                 "font: bold 11pt 'Segoe UI'; "
                                                 "background: transparent;")
        self.label_stockout_reason.setObjectName("label_stockout_reason")

        self.combo_stockout_reason = QtWidgets.QComboBox(parent=self.frame_stockout_form)
        self.combo_stockout_reason.setGeometry(QtCore.QRect(610, 170, 530, 45))
        self.combo_stockout_reason.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QComboBox:focus { border: 2px solid rgb(52, 152, 219); }
            QComboBox QAbstractItemView {
                background-color: white; color: black;
                selection-background-color: rgb(52, 152, 219);
                selection-color: white;
            }
        """)
        self.combo_stockout_reason.addItem("Select Reason")
        self.combo_stockout_reason.addItem("Sold")
        self.combo_stockout_reason.addItem("Used for Repair")
        self.combo_stockout_reason.addItem("Damaged")
        self.combo_stockout_reason.addItem("Defective/RMA")
        self.combo_stockout_reason.addItem("Other")
        self.combo_stockout_reason.setObjectName("combo_stockout_reason")

        self.label_stockout_notes = QtWidgets.QLabel(parent=self.frame_stockout_form)
        self.label_stockout_notes.setGeometry(QtCore.QRect(40, 240, 200, 25))
        self.label_stockout_notes.setStyleSheet("color: rgb(52, 73, 94); "
                                                "font: bold 11pt 'Segoe UI'; "
                                                "background: transparent;")
        self.label_stockout_notes.setObjectName("label_stockout_notes")

        self.input_stockout_notes = QtWidgets.QTextEdit(parent=self.frame_stockout_form)
        self.input_stockout_notes.setGeometry(QtCore.QRect(40, 270, 1100, 100))
        self.input_stockout_notes.setStyleSheet("""
            QTextEdit {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding: 10px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QTextEdit:focus { border: 2px solid rgb(52, 152, 219); }
        """)
        self.input_stockout_notes.setObjectName("input_stockout_notes")

        self.btn_record_stockout = QtWidgets.QPushButton(parent=self.frame_stockout_form)
        self.btn_record_stockout.setGeometry(QtCore.QRect(40, 395, 1100, 55))
        self.btn_record_stockout.setStyleSheet("""
            QPushButton {
                background-color: rgb(230, 126, 34);
                color: white;
                border: none;
                border-radius: 5px;
                font: bold 13pt 'Segoe UI';
            }
            QPushButton:hover { background-color: rgb(211, 84, 0); }
            QPushButton:pressed { background-color: rgb(186, 74, 0); }
        """)
        self.btn_record_stockout.setObjectName("btn_record_stockout")

        self.tab_widget.addTab(self.tab_stockout, "")

        # ===========================
        # TAB 5: VIEW INVENTORY
        # ===========================
        self.tab_inventory = QtWidgets.QWidget()
        self.tab_inventory.setObjectName("tab_inventory")

        self.label_inventory_title = QtWidgets.QLabel(parent=self.tab_inventory)
        self.label_inventory_title.setGeometry(QtCore.QRect(30, 20, 300, 35))
        self.label_inventory_title.setStyleSheet("color: rgb(52, 73, 94); "
                                                 "font: bold 18pt 'Segoe UI'; "
                                                 "background: transparent;")
        self.label_inventory_title.setObjectName("label_inventory_title")

        self.input_search = QtWidgets.QLineEdit(parent=self.tab_inventory)
        self.input_search.setGeometry(QtCore.QRect(880, 20, 330, 40))
        self.input_search.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid rgb(189, 195, 199);
                border-radius: 5px;
                padding-left: 15px;
                font: 10pt 'Segoe UI';
                color: black;
            }
            QLineEdit:focus { border: 2px solid rgb(52, 152, 219); }
        """)
        self.input_search.setObjectName("input_search")

        self.table_inventory = QtWidgets.QTableWidget(parent=self.tab_inventory)
        self.table_inventory.setGeometry(QtCore.QRect(30, 80, 1180, 470))
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
        self.table_inventory.setRowCount(0)
        self.table_inventory.setHorizontalHeaderLabels(
            ["Item Name", "Category", "Current Stock", "Min Stock", "Price", "Status"]
        )
        self.table_inventory.horizontalHeader().setStretchLastSection(True)
        self.table_inventory.setColumnWidth(0, 300)
        self.table_inventory.setColumnWidth(1, 200)
        self.table_inventory.setColumnWidth(2, 130)
        self.table_inventory.setColumnWidth(3, 120)
        self.table_inventory.setColumnWidth(4, 130)
        self.table_inventory.verticalHeader().setVisible(False)
        self.table_inventory.setAlternatingRowColors(True)
        self.table_inventory.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_inventory.setObjectName("table_inventory")

        self.tab_widget.addTab(self.tab_inventory, "")

        self.tab_widget.setCurrentIndex(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("StaffDashboard", "Inventory System - Staff Dashboard"))

        self.label_title.setText(_translate("StaffDashboard", "COMPTRACK"))
        self.label_user.setText(_translate("StaffDashboard", "Logged in as: Staff"))
        self.btn_logout.setText(_translate("StaffDashboard", "Logout"))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_dashboard),
                                   _translate("StaffDashboard", "Dashboard"))
        self.label_total_title.setText(_translate("StaffDashboard", "Total Items"))
        self.label_total_value.setText(_translate("StaffDashboard", "0"))
        self.label_lowstock_title.setText(_translate("StaffDashboard", "Low Stock Alert"))
        self.label_lowstock_value.setText(_translate("StaffDashboard", "0"))
        self.label_stockin_title.setText(_translate("StaffDashboard", "Stock In (Today)"))
        self.label_stockin_value.setText(_translate("StaffDashboard", "0"))
        self.label_stockout_title.setText(_translate("StaffDashboard", "Stock Out (Today)"))
        self.label_stockout_value.setText(_translate("StaffDashboard", "0"))
        self.label_recent.setText(_translate("StaffDashboard", "Recent Transactions"))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_additem),
                                   _translate("StaffDashboard", "Add Item"))
        self.label_additem_page.setText(_translate("StaffDashboard", "Add New Item"))
        self.label_additem_name.setText(_translate("StaffDashboard", "Item Name"))
        self.input_additem_name.setPlaceholderText(_translate("StaffDashboard", "e.g., Intel Core i7-13700K"))
        self.label_additem_category.setText(_translate("StaffDashboard", "Category"))
        self.label_additem_stock.setText(_translate("StaffDashboard", "Initial Stock"))
        self.input_additem_stock.setPlaceholderText(_translate("StaffDashboard", "Enter initial quantity"))
        self.label_additem_minstock.setText(_translate("StaffDashboard", "Minimum Stock"))
        self.input_additem_minstock.setPlaceholderText(_translate("StaffDashboard", "Alert threshold"))
        self.label_additem_price.setText(_translate("StaffDashboard", "Unit Price"))
        self.input_additem_price.setPlaceholderText(_translate("StaffDashboard", "Price per unit"))
        self.btn_add_newitem.setText(_translate("StaffDashboard", "➕ Add Item to Inventory"))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_stockin),
                                   _translate("StaffDashboard", "Stock In"))
        self.label_stockin_page.setText(_translate("StaffDashboard", "Record Stock In"))
        self.label_stockin_item.setText(_translate("StaffDashboard", "Select Item"))
        self.combo_stockin_item.setPlaceholderText(_translate("StaffDashboard", "Choose an item..."))
        self.label_stockin_qty.setText(_translate("StaffDashboard", "Quantity"))
        self.input_stockin_qty.setPlaceholderText(_translate("StaffDashboard", "Enter quantity to add"))
        self.label_stockin_notes.setText(_translate("StaffDashboard", "Notes (Optional)"))
        self.input_stockin_notes.setPlaceholderText(_translate("StaffDashboard", "Add any additional notes..."))
        self.btn_record_stockin.setText(_translate("StaffDashboard", "✓ Record Stock In"))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_stockout),
                                   _translate("StaffDashboard", "Stock Out"))
        self.label_stockout_page.setText(_translate("StaffDashboard", "Record Stock Out"))
        self.label_stockout_item.setText(_translate("StaffDashboard", "Select Item"))
        self.combo_stockout_item.setPlaceholderText(_translate("StaffDashboard", "Choose an item..."))
        self.label_stockout_qty.setText(_translate("StaffDashboard", "Quantity"))
        self.input_stockout_qty.setPlaceholderText(_translate("StaffDashboard", "Enter quantity to deduct"))
        self.label_stockout_reason.setText(_translate("StaffDashboard", "Reason"))
        self.label_stockout_notes.setText(_translate("StaffDashboard", "Notes (Optional)"))
        self.input_stockout_notes.setPlaceholderText(_translate("StaffDashboard", "Add any additional notes..."))
        self.btn_record_stockout.setText(_translate("StaffDashboard", "⚠ Record Stock Out"))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_inventory),
                                   _translate("StaffDashboard", "View Inventory"))
        self.label_inventory_title.setText(_translate("StaffDashboard", "Current Inventory"))
        self.input_search.setPlaceholderText(_translate("StaffDashboard", "Search items..."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_StaffDashboard()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())