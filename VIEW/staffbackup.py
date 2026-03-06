# Staff Dashboard UI - Resizable (layout-based)
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QSizePolicy

LOGO_PATH = r"C:\Users\asus\PycharmProjects\Inventory_System_Final\SOURCE\logo.png"

INPUT_STYLE = """
    QLineEdit {
        background-color: white;
        border: 2px solid rgb(189, 195, 199);
        border-radius: 5px;
        padding-left: 15px;
        font: 10pt 'Segoe UI';
        color: black;
    }
    QLineEdit:focus { border: 2px solid rgb(52, 152, 219); }
"""

COMBO_STYLE = """
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
"""

TEXTEDIT_STYLE = """
    QTextEdit {
        background-color: white;
        border: 2px solid rgb(189, 195, 199);
        border-radius: 5px;
        padding: 10px;
        font: 10pt 'Segoe UI';
        color: black;
    }
    QTextEdit:focus { border: 2px solid rgb(52, 152, 219); }
"""

LABEL_FIELD = "color: rgb(52, 73, 94); font: bold 11pt 'Segoe UI'; background: transparent;"
LABEL_SECTION = "color: rgb(52, 73, 94); font: bold 18pt 'Segoe UI'; background: transparent;"
LABEL_CARD_TITLE = "color: rgba(255,255,255,200); font: 10pt 'Segoe UI'; background: transparent;"
LABEL_CARD_VALUE = "color: white; font: bold 32pt 'Segoe UI'; background: transparent;"

TABLE_STYLE = """
    QTableWidget {
        background-color: white;
        border: 1px solid rgb(189, 195, 199);
        border-radius: 5px;
        gridline-color: rgb(236, 240, 241);
        color: black;
    }
    QHeaderView::section {
        background-color: rgb(52, 73, 94);
        color: white;
        padding: 8px;
        border: none;
        font: bold 10pt 'Segoe UI';
    }
"""

FORM_FRAME_STYLE = """
    QFrame {
        background-color: rgb(250, 251, 252);
        border: 2px solid rgb(189, 195, 199);
        border-radius: 10px;
    }
"""


def _make_logo_pixmap(size=50):
    px = QtGui.QPixmap(LOGO_PATH)
    if not px.isNull():
        return px.scaled(size, size,
                         QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                         QtCore.Qt.TransformationMode.SmoothTransformation)
    return None


class Ui_StaffDashboard(object):
    def setupUi(self, Form):
        Form.setObjectName("StaffDashboard")
        Form.resize(1280, 720)
        Form.setMinimumSize(900, 600)

        # Support both QMainWindow (controller) and QWidget (standalone test)
        if isinstance(Form, QtWidgets.QMainWindow):
            self.centralwidget = QtWidgets.QWidget(Form)
            self.centralwidget.setStyleSheet("background-color: rgb(236, 240, 241);")
            Form.setCentralWidget(self.centralwidget)
            container = self.centralwidget
        else:
            Form.setStyleSheet("background-color: rgb(236, 240, 241);")
            container = Form

        root = QVBoxLayout(container)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── HEADER ──────────────────────────────────────────────────────────
        self.frame_header = QtWidgets.QFrame()
        self.frame_header.setFixedHeight(70)
        self.frame_header.setStyleSheet("QFrame { background-color: rgb(52, 73, 94); }")
        self.frame_header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_header.setObjectName("frame_header")

        hdr = QHBoxLayout(self.frame_header)
        hdr.setContentsMargins(20, 10, 20, 10)
        hdr.setSpacing(12)

        self.label_logo_image = QtWidgets.QLabel()
        self.label_logo_image.setFixedSize(70, 50)
        self.label_logo_image.setStyleSheet("background: white; margin: 2px; border-radius: 3px;")
        self.label_logo_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_logo_image.setObjectName("label_logo_image")
        px = _make_logo_pixmap(50)
        if px:
            self.label_logo_image.setPixmap(px)
        hdr.addWidget(self.label_logo_image)

        self.label_title = QtWidgets.QLabel()
        self.label_title.setStyleSheet("color: white; font: bold 20pt 'Segoe UI'; background: transparent;")
        self.label_title.setObjectName("label_title")
        hdr.addWidget(self.label_title)

        hdr.addStretch()

        self.label_user = QtWidgets.QLabel()
        self.label_user.setStyleSheet("color: rgb(189, 195, 199); font: 11pt 'Segoe UI'; background: transparent;")
        self.label_user.setObjectName("label_user")
        hdr.addWidget(self.label_user)

        self.btn_logout = QtWidgets.QPushButton()
        self.btn_logout.setFixedSize(100, 40)
        self.btn_logout.setStyleSheet("""
            QPushButton { background-color: rgb(231,76,60); color: white; border: none;
                          border-radius: 5px; font: bold 10pt 'Segoe UI'; }
            QPushButton:hover { background-color: rgb(192,57,43); }
        """)
        self.btn_logout.setObjectName("btn_logout")
        hdr.addWidget(self.btn_logout)

        root.addWidget(self.frame_header)

        # ── TAB WIDGET ───────────────────────────────────────────────────────
        tab_wrap = QtWidgets.QWidget()
        tab_wrap_layout = QVBoxLayout(tab_wrap)
        tab_wrap_layout.setContentsMargins(15, 15, 15, 15)

        self.tab_widget = QtWidgets.QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid rgb(189,195,199);
                border-radius: 5px;
                background-color: white;
            }
            QTabBar::tab {
                background-color: rgb(189,195,199);
                color: rgb(52,73,94);
                padding: 10px 22px;
                margin-right: 2px;
                font: bold 10pt 'Segoe UI';
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
            }
            QTabBar::tab:selected { background-color: rgb(52,152,219); color: white; }
            QTabBar::tab:hover:!selected { background-color: rgb(149,165,166); }
        """)
        self.tab_widget.setObjectName("tab_widget")

        self._build_tab_dashboard()
        self._build_tab_additem()
        self._build_tab_stockin()
        self._build_tab_stockout()
        self._build_tab_inventory()

        self.tab_widget.setCurrentIndex(0)
        tab_wrap_layout.addWidget(self.tab_widget)
        root.addWidget(tab_wrap)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # ── helpers ─────────────────────────────────────────────────────────────

    def _make_card(self, color):
        card = QtWidgets.QFrame()
        card.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        card.setMinimumHeight(100)
        card.setStyleSheet(f"QFrame {{ background-color: {color}; border-radius: 10px; }}")
        lay = QVBoxLayout(card)
        lay.setContentsMargins(20, 12, 20, 12)
        lay.setSpacing(4)
        t = QtWidgets.QLabel()
        t.setStyleSheet(LABEL_CARD_TITLE)
        v = QtWidgets.QLabel()
        v.setStyleSheet(LABEL_CARD_VALUE)
        lay.addWidget(t)
        lay.addWidget(v)
        return card, t, v

    def _field_label(self):
        lbl = QtWidgets.QLabel()
        lbl.setStyleSheet(LABEL_FIELD)
        return lbl

    def _line_edit(self):
        w = QtWidgets.QLineEdit()
        w.setFixedHeight(42)
        w.setStyleSheet(INPUT_STYLE)
        return w

    def _combo(self):
        w = QtWidgets.QComboBox()
        w.setFixedHeight(42)
        w.setStyleSheet(COMBO_STYLE)
        return w

    def _table(self, cols, headers):
        t = QtWidgets.QTableWidget()
        t.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        t.setStyleSheet(TABLE_STYLE)
        t.setColumnCount(cols)
        t.setHorizontalHeaderLabels(headers)
        t.horizontalHeader().setStretchLastSection(True)
        t.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Interactive)
        t.verticalHeader().setVisible(False)
        t.setAlternatingRowColors(True)
        t.setRowCount(0)
        return t

    def _form_frame(self):
        f = QtWidgets.QFrame()
        f.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        f.setStyleSheet(FORM_FRAME_STYLE)
        return f

    # ── TAB 1: DASHBOARD ────────────────────────────────────────────────────

    def _build_tab_dashboard(self):
        self.tab_dashboard = QtWidgets.QWidget()
        self.tab_dashboard.setObjectName("tab_dashboard")
        lay = QVBoxLayout(self.tab_dashboard)
        lay.setContentsMargins(25, 20, 25, 20)
        lay.setSpacing(15)

        cards_row = QHBoxLayout()
        cards_row.setSpacing(15)

        self.card_total, self.label_total_title, self.label_total_value = \
            self._make_card("rgb(52,152,219)")
        self.card_total.setObjectName("card_total")
        self.label_total_title.setObjectName("label_total_title")
        self.label_total_value.setObjectName("label_total_value")

        self.card_lowstock, self.label_lowstock_title, self.label_lowstock_value = \
            self._make_card("rgb(231,76,60)")
        self.card_lowstock.setObjectName("card_lowstock")
        self.label_lowstock_title.setObjectName("label_lowstock_title")
        self.label_lowstock_value.setObjectName("label_lowstock_value")

        self.card_stockin, self.label_stockin_title, self.label_stockin_value = \
            self._make_card("rgb(46,204,113)")
        self.card_stockin.setObjectName("card_stockin")
        self.label_stockin_title.setObjectName("label_stockin_title")
        self.label_stockin_value.setObjectName("label_stockin_value")

        self.card_stockout, self.label_stockout_title, self.label_stockout_value = \
            self._make_card("rgb(230,126,34)")
        self.card_stockout.setObjectName("card_stockout")
        self.label_stockout_title.setObjectName("label_stockout_title")
        self.label_stockout_value.setObjectName("label_stockout_value")

        for c in [self.card_total, self.card_lowstock, self.card_stockin, self.card_stockout]:
            cards_row.addWidget(c)
        lay.addLayout(cards_row)

        self.label_recent = QtWidgets.QLabel()
        self.label_recent.setStyleSheet(
            "color: rgb(52,73,94); font: bold 14pt 'Segoe UI'; background: transparent;")
        self.label_recent.setObjectName("label_recent")
        lay.addWidget(self.label_recent)

        self.table_recent = self._table(
            6, ["Date & Time", "Item Name", "Type", "Quantity", "Performed By", "Notes"])
        self.table_recent.setObjectName("table_recent")
        lay.addWidget(self.table_recent)

        self.tab_widget.addTab(self.tab_dashboard, "")

    # ── TAB 2: ADD ITEM ──────────────────────────────────────────────────────

    def _build_tab_additem(self):
        self.tab_additem = QtWidgets.QWidget()
        self.tab_additem.setObjectName("tab_additem")
        outer = QVBoxLayout(self.tab_additem)
        outer.setContentsMargins(25, 20, 25, 20)
        outer.setSpacing(15)

        self.label_additem_page = QtWidgets.QLabel()
        self.label_additem_page.setStyleSheet(LABEL_SECTION)
        self.label_additem_page.setObjectName("label_additem_page")
        outer.addWidget(self.label_additem_page)

        frame = self._form_frame()
        fl = QVBoxLayout(frame)
        fl.setContentsMargins(30, 25, 30, 25)
        fl.setSpacing(12)

        self.label_additem_name = self._field_label()
        self.label_additem_name.setObjectName("label_additem_name")
        fl.addWidget(self.label_additem_name)
        self.input_additem_name = self._line_edit()
        self.input_additem_name.setObjectName("input_additem_name")
        fl.addWidget(self.input_additem_name)

        self.label_additem_category = self._field_label()
        self.label_additem_category.setObjectName("label_additem_category")
        fl.addWidget(self.label_additem_category)
        self.combo_additem_category = self._combo()
        self.combo_additem_category.setObjectName("combo_additem_category")
        for item in ["Select Category", "CPU (Processor)", "GPU (Graphics Card)",
                     "RAM (Memory)", "Storage (SSD/HDD)", "Motherboard",
                     "Power Supply", "Case/Chassis", "Cooling", "Peripherals",
                     "Accessories", "Other"]:
            self.combo_additem_category.addItem(item)
        fl.addWidget(self.combo_additem_category)

        row3 = QHBoxLayout()
        row3.setSpacing(20)

        col_stock = QVBoxLayout()
        self.label_additem_stock = self._field_label()
        self.label_additem_stock.setObjectName("label_additem_stock")
        self.input_additem_stock = self._line_edit()
        self.input_additem_stock.setObjectName("input_additem_stock")
        col_stock.addWidget(self.label_additem_stock)
        col_stock.addWidget(self.input_additem_stock)

        col_min = QVBoxLayout()
        self.label_additem_minstock = self._field_label()
        self.label_additem_minstock.setObjectName("label_additem_minstock")
        self.input_additem_minstock = self._line_edit()
        self.input_additem_minstock.setObjectName("input_additem_minstock")
        col_min.addWidget(self.label_additem_minstock)
        col_min.addWidget(self.input_additem_minstock)

        col_price = QVBoxLayout()
        self.label_additem_price = self._field_label()
        self.label_additem_price.setObjectName("label_additem_price")
        self.input_additem_price = self._line_edit()
        self.input_additem_price.setObjectName("input_additem_price")
        col_price.addWidget(self.label_additem_price)
        col_price.addWidget(self.input_additem_price)

        row3.addLayout(col_stock)
        row3.addLayout(col_min)
        row3.addLayout(col_price)
        fl.addLayout(row3)

        fl.addStretch()

        self.btn_add_newitem = QtWidgets.QPushButton()
        self.btn_add_newitem.setFixedHeight(50)
        self.btn_add_newitem.setStyleSheet("""
            QPushButton { background-color: rgb(52,152,219); color: white; border: none;
                          border-radius: 5px; font: bold 13pt 'Segoe UI'; }
            QPushButton:hover { background-color: rgb(41,128,185); }
            QPushButton:pressed { background-color: rgb(31,97,141); }
        """)
        self.btn_add_newitem.setObjectName("btn_add_newitem")
        fl.addWidget(self.btn_add_newitem)

        outer.addWidget(frame)
        self.tab_widget.addTab(self.tab_additem, "")

    # ── TAB 3: STOCK IN ──────────────────────────────────────────────────────

    def _build_tab_stockin(self):
        self.tab_stockin = QtWidgets.QWidget()
        self.tab_stockin.setObjectName("tab_stockin")
        outer = QVBoxLayout(self.tab_stockin)
        outer.setContentsMargins(25, 20, 25, 20)
        outer.setSpacing(15)

        self.label_stockin_page = QtWidgets.QLabel()
        self.label_stockin_page.setStyleSheet(LABEL_SECTION)
        self.label_stockin_page.setObjectName("label_stockin_page")
        outer.addWidget(self.label_stockin_page)

        frame = self._form_frame()
        fl = QVBoxLayout(frame)
        fl.setContentsMargins(30, 25, 30, 25)
        fl.setSpacing(12)

        row1 = QHBoxLayout()
        row1.setSpacing(20)

        col_item = QVBoxLayout()
        self.label_stockin_item = self._field_label()
        self.label_stockin_item.setObjectName("label_stockin_item")
        self.combo_stockin_item = self._combo()
        self.combo_stockin_item.setObjectName("combo_stockin_item")
        col_item.addWidget(self.label_stockin_item)
        col_item.addWidget(self.combo_stockin_item)

        col_qty = QVBoxLayout()
        self.label_stockin_qty = self._field_label()
        self.label_stockin_qty.setObjectName("label_stockin_qty")
        self.input_stockin_qty = self._line_edit()
        self.input_stockin_qty.setObjectName("input_stockin_qty")
        col_qty.addWidget(self.label_stockin_qty)
        col_qty.addWidget(self.input_stockin_qty)

        row1.addLayout(col_item)
        row1.addLayout(col_qty)
        fl.addLayout(row1)

        self.label_stockin_notes = self._field_label()
        self.label_stockin_notes.setObjectName("label_stockin_notes")
        fl.addWidget(self.label_stockin_notes)
        self.input_stockin_notes = QtWidgets.QTextEdit()
        self.input_stockin_notes.setFixedHeight(100)
        self.input_stockin_notes.setStyleSheet(TEXTEDIT_STYLE)
        self.input_stockin_notes.setObjectName("input_stockin_notes")
        fl.addWidget(self.input_stockin_notes)

        fl.addStretch()

        self.btn_record_stockin = QtWidgets.QPushButton()
        self.btn_record_stockin.setFixedHeight(50)
        self.btn_record_stockin.setStyleSheet("""
            QPushButton { background-color: rgb(46,204,113); color: white; border: none;
                          border-radius: 5px; font: bold 13pt 'Segoe UI'; }
            QPushButton:hover { background-color: rgb(39,174,96); }
            QPushButton:pressed { background-color: rgb(34,153,84); }
        """)
        self.btn_record_stockin.setObjectName("btn_record_stockin")
        fl.addWidget(self.btn_record_stockin)

        outer.addWidget(frame)
        self.tab_widget.addTab(self.tab_stockin, "")

    # ── TAB 4: STOCK OUT ─────────────────────────────────────────────────────

    def _build_tab_stockout(self):
        self.tab_stockout = QtWidgets.QWidget()
        self.tab_stockout.setObjectName("tab_stockout")
        outer = QVBoxLayout(self.tab_stockout)
        outer.setContentsMargins(25, 20, 25, 20)
        outer.setSpacing(15)

        self.label_stockout_page = QtWidgets.QLabel()
        self.label_stockout_page.setStyleSheet(LABEL_SECTION)
        self.label_stockout_page.setObjectName("label_stockout_page")
        outer.addWidget(self.label_stockout_page)

        frame = self._form_frame()
        fl = QVBoxLayout(frame)
        fl.setContentsMargins(30, 25, 30, 25)
        fl.setSpacing(12)

        self.label_stockout_item = self._field_label()
        self.label_stockout_item.setObjectName("label_stockout_item")
        fl.addWidget(self.label_stockout_item)
        self.combo_stockout_item = self._combo()
        self.combo_stockout_item.setObjectName("combo_stockout_item")
        fl.addWidget(self.combo_stockout_item)

        row2 = QHBoxLayout()
        row2.setSpacing(20)

        col_qty = QVBoxLayout()
        self.label_stockout_qty = self._field_label()
        self.label_stockout_qty.setObjectName("label_stockout_qty")
        self.input_stockout_qty = self._line_edit()
        self.input_stockout_qty.setObjectName("input_stockout_qty")
        col_qty.addWidget(self.label_stockout_qty)
        col_qty.addWidget(self.input_stockout_qty)

        col_reason = QVBoxLayout()
        self.label_stockout_reason = self._field_label()
        self.label_stockout_reason.setObjectName("label_stockout_reason")
        self.combo_stockout_reason = self._combo()
        for r in ["Select Reason", "Sold", "Used for Repair", "Damaged", "Defective/RMA", "Other"]:
            self.combo_stockout_reason.addItem(r)
        self.combo_stockout_reason.setObjectName("combo_stockout_reason")
        col_reason.addWidget(self.label_stockout_reason)
        col_reason.addWidget(self.combo_stockout_reason)

        row2.addLayout(col_qty)
        row2.addLayout(col_reason)
        fl.addLayout(row2)

        self.label_stockout_notes = self._field_label()
        self.label_stockout_notes.setObjectName("label_stockout_notes")
        fl.addWidget(self.label_stockout_notes)
        self.input_stockout_notes = QtWidgets.QTextEdit()
        self.input_stockout_notes.setFixedHeight(100)
        self.input_stockout_notes.setStyleSheet(TEXTEDIT_STYLE)
        self.input_stockout_notes.setObjectName("input_stockout_notes")
        fl.addWidget(self.input_stockout_notes)

        fl.addStretch()

        self.btn_record_stockout = QtWidgets.QPushButton()
        self.btn_record_stockout.setFixedHeight(50)
        self.btn_record_stockout.setStyleSheet("""
            QPushButton { background-color: rgb(230,126,34); color: white; border: none;
                          border-radius: 5px; font: bold 13pt 'Segoe UI'; }
            QPushButton:hover { background-color: rgb(211,84,0); }
            QPushButton:pressed { background-color: rgb(186,74,0); }
        """)
        self.btn_record_stockout.setObjectName("btn_record_stockout")
        fl.addWidget(self.btn_record_stockout)

        outer.addWidget(frame)
        self.tab_widget.addTab(self.tab_stockout, "")

    # ── TAB 5: VIEW INVENTORY ────────────────────────────────────────────────

    def _build_tab_inventory(self):
        self.tab_inventory = QtWidgets.QWidget()
        self.tab_inventory.setObjectName("tab_inventory")
        outer = QVBoxLayout(self.tab_inventory)
        outer.setContentsMargins(25, 20, 25, 20)
        outer.setSpacing(15)

        top = QHBoxLayout()
        self.label_inventory_title = QtWidgets.QLabel()
        self.label_inventory_title.setStyleSheet(LABEL_SECTION)
        self.label_inventory_title.setObjectName("label_inventory_title")
        top.addWidget(self.label_inventory_title)
        top.addStretch()

        self.input_search = QtWidgets.QLineEdit()
        self.input_search.setFixedSize(280, 40)
        self.input_search.setStyleSheet(INPUT_STYLE)
        self.input_search.setObjectName("input_search")
        top.addWidget(self.input_search)
        outer.addLayout(top)

        self.table_inventory = self._table(
            6, ["Item Name", "Category", "Current Stock", "Min Stock", "Price", "Status"])
        self.table_inventory.setObjectName("table_inventory")
        outer.addWidget(self.table_inventory)

        self.tab_widget.addTab(self.tab_inventory, "")

    # ── retranslate ──────────────────────────────────────────────────────────

    def retranslateUi(self, Form):
        _ = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_("StaffDashboard", "Inventory System - Staff Dashboard"))

        self.label_title.setText(_("StaffDashboard", "COMPUTER INVENTORY"))
        self.label_user.setText(_("StaffDashboard", "Logged in as: Staff"))
        self.btn_logout.setText(_("StaffDashboard", "Logout"))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_dashboard),
                                   _("StaffDashboard", "Dashboard"))
        self.label_total_title.setText(_("StaffDashboard", "Total Items"))
        self.label_total_value.setText(_("StaffDashboard", "0"))
        self.label_lowstock_title.setText(_("StaffDashboard", "Low Stock Alert"))
        self.label_lowstock_value.setText(_("StaffDashboard", "0"))
        self.label_stockin_title.setText(_("StaffDashboard", "Stock In (Today)"))
        self.label_stockin_value.setText(_("StaffDashboard", "0"))
        self.label_stockout_title.setText(_("StaffDashboard", "Stock Out (Today)"))
        self.label_stockout_value.setText(_("StaffDashboard", "0"))
        self.label_recent.setText(_("StaffDashboard", "Recent Transactions"))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_additem),
                                   _("StaffDashboard", "Add Item"))
        self.label_additem_page.setText(_("StaffDashboard", "Add New Item"))
        self.label_additem_name.setText(_("StaffDashboard", "Item Name"))
        self.input_additem_name.setPlaceholderText(_("StaffDashboard", "e.g., Intel Core i7-13700K"))
        self.label_additem_category.setText(_("StaffDashboard", "Category"))
        self.label_additem_stock.setText(_("StaffDashboard", "Initial Stock"))
        self.input_additem_stock.setPlaceholderText(_("StaffDashboard", "Enter initial quantity"))
        self.label_additem_minstock.setText(_("StaffDashboard", "Minimum Stock"))
        self.input_additem_minstock.setPlaceholderText(_("StaffDashboard", "Alert threshold"))
        self.label_additem_price.setText(_("StaffDashboard", "Unit Price"))
        self.input_additem_price.setPlaceholderText(_("StaffDashboard", "Price per unit"))
        self.btn_add_newitem.setText(_("StaffDashboard", "➕ Add Item to Inventory"))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_stockin),
                                   _("StaffDashboard", "Stock In"))
        self.label_stockin_page.setText(_("StaffDashboard", "Record Stock In"))
        self.label_stockin_item.setText(_("StaffDashboard", "Select Item"))
        self.combo_stockin_item.setPlaceholderText(_("StaffDashboard", "Choose an item..."))
        self.label_stockin_qty.setText(_("StaffDashboard", "Quantity"))
        self.input_stockin_qty.setPlaceholderText(_("StaffDashboard", "Enter quantity to add"))
        self.label_stockin_notes.setText(_("StaffDashboard", "Notes (Optional)"))
        self.input_stockin_notes.setPlaceholderText(_("StaffDashboard", "Add any additional notes..."))
        self.btn_record_stockin.setText(_("StaffDashboard", "✓ Record Stock In"))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_stockout),
                                   _("StaffDashboard", "Stock Out"))
        self.label_stockout_page.setText(_("StaffDashboard", "Record Stock Out"))
        self.label_stockout_item.setText(_("StaffDashboard", "Select Item"))
        self.combo_stockout_item.setPlaceholderText(_("StaffDashboard", "Choose an item..."))
        self.label_stockout_qty.setText(_("StaffDashboard", "Quantity"))
        self.input_stockout_qty.setPlaceholderText(_("StaffDashboard", "Enter quantity to deduct"))
        self.label_stockout_reason.setText(_("StaffDashboard", "Reason"))
        self.label_stockout_notes.setText(_("StaffDashboard", "Notes (Optional)"))
        self.input_stockout_notes.setPlaceholderText(_("StaffDashboard", "Add any additional notes..."))
        self.btn_record_stockout.setText(_("StaffDashboard", "⚠ Record Stock Out"))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_inventory),
                                   _("StaffDashboard", "View Inventory"))
        self.label_inventory_title.setText(_("StaffDashboard", "Current Inventory"))
        self.input_search.setPlaceholderText(_("StaffDashboard", "Search items..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_StaffDashboard()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())