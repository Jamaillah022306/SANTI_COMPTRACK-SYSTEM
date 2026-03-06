from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QHeaderView
from PyQt6.QtCore import Qt
from VIEW.staff_v import Ui_StaffDashboard
from VIEW.message import Ui_message
from MODEL.staff_m import staffM


class staff(QMainWindow):
    def __init__(self, manager=None, name=""):
        super().__init__()
        self.ui = Ui_StaffDashboard()
        self.ui.setupUi(self)
        self.mes = Ui_message()
        self.manager = manager
        self.name = name

        # Connect buttons
        self.ui.btn_logout.clicked.connect(self.logout)
        self.ui.btn_add_newitem.clicked.connect(self.addItem)
        self.ui.btn_record_stockin.clicked.connect(self.stockIn_tab)
        self.ui.btn_record_stockout.clicked.connect(self.stockOut_tab)

        # Connect search
        self.ui.input_search.textChanged.connect(self.on_search_inventory)

        # Make low stock card clickable
        self.ui.card_lowstock.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.card_lowstock.mousePressEvent = lambda e: self.show_lowstock_dialog()

        # Set user label
        self.ui.label_user.setText(f"Welcome, {self.name}")

        # Initial data
        self.refresh()
        self.count()
        self.populateComboBoxes()

    # -------- Logout --------
    def logout(self):
        self.manager.show_login()

    # -------- Low Stock Dialog --------
    def show_lowstock_dialog(self):
        items = staffM.getLowStockItems()

        dialog = QDialog()
        dialog.setWindowTitle("⚠ Low Stock Alert")
        dialog.setFixedSize(600, 400)
        dialog.setStyleSheet("""
            QDialog { background-color: white; }
            QLabel#title { color: rgb(192, 57, 43); font: bold 14pt 'Segoe UI'; }
            QLabel#subtitle { color: rgb(100, 100, 100); font: 10pt 'Segoe UI'; }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # Title
        title = QLabel(f"⚠  {len(items)} Item(s) Need Restocking!")
        title.setObjectName("title")
        title.setStyleSheet("color: rgb(192, 57, 43); font: bold 14pt 'Segoe UI';")
        layout.addWidget(title)

        subtitle = QLabel("The following items have reached or fallen below minimum stock level.")
        subtitle.setObjectName("subtitle")
        subtitle.setStyleSheet("color: rgb(100, 100, 100); font: 10pt 'Segoe UI';")
        layout.addWidget(subtitle)

        # Table
        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Item Name", "Category", "Current Stock", "Min Stock"])
        table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid rgb(189, 195, 199);
                border-radius: 5px;
                color: black;
            }
            QHeaderView::section {
                background-color: rgb(192, 57, 43);
                color: white;
                padding: 8px;
                font: bold 10pt 'Segoe UI';
            }
            QTableWidget::item { color: black; }
        """)
        table.setRowCount(0)
        table.verticalHeader().setVisible(False)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.setAlternatingRowColors(True)

        for row, item in enumerate(items):
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(str(item['item_name'])))
            table.setItem(row, 1, QTableWidgetItem(str(item['category'])))

            stock_item = QTableWidgetItem(str(item['stock']))
            stock_item.setForeground(Qt.GlobalColor.red)
            table.setItem(row, 2, stock_item)
            table.setItem(row, 3, QTableWidgetItem(str(item['min_stock'])))

        layout.addWidget(table)

        # Close button
        btn_close = QPushButton("Close")
        btn_close.setFixedHeight(40)
        btn_close.setStyleSheet("""
            QPushButton {
                background-color: rgb(192, 57, 43);
                color: white;
                border-radius: 5px;
                font: bold 10pt 'Segoe UI';
            }
            QPushButton:hover { background-color: rgb(169, 50, 38); }
        """)
        btn_close.clicked.connect(dialog.accept)
        layout.addWidget(btn_close)

        dialog.setLayout(layout)
        dialog.exec()

    # -------- Custom Success Dialog --------
    def show_success(self, message):
        dialog = QDialog()
        dialog.setWindowTitle("Success")
        dialog.setStyleSheet("background-color: white;")
        dialog.setFixedSize(300, 120)

        layout = QVBoxLayout()

        label = QLabel(message)
        label.setStyleSheet("color: black; font: 11pt 'Segoe UI';")

        btn_ok = QPushButton("OK")
        btn_ok.setStyleSheet("""
            QPushButton {
                background-color: rgb(46, 204, 113);
                color: white;
                border-radius: 5px;
                padding: 5px 20px;
                font: bold 10pt 'Segoe UI';
            }
            QPushButton:hover { background-color: rgb(39, 174, 96); }
        """)
        btn_ok.clicked.connect(dialog.accept)

        layout.addWidget(label)
        layout.addWidget(btn_ok)
        dialog.setLayout(layout)
        dialog.exec()

    # -------- Refresh Tables --------
    def refresh(self):
        self.fillTable(self.ui.table_recent, staffM.recenttransaction())
        self.fillTable(self.ui.table_inventory, staffM.currentinventory())

    # -------- Count Info --------
    def count(self):
        total = staffM.totalItem()
        lowstock = staffM.lowStock()
        stockIn = staffM.stocks("IN")
        stockOut = staffM.stocks("OUT")
        self.ui.label_total_value.setText(str(total['total']))
        self.ui.label_lowstock_value.setText(str(lowstock['total']))
        self.ui.label_stockin_value.setText(str(stockIn['total']))
        self.ui.label_stockout_value.setText(str(stockOut['total']))

    # -------- Fill Table --------
    def fillTable(self, table, data, search_text=""):
        if not table:
            return
        table.setRowCount(0)

        for row_data in data:
            if table == self.ui.table_inventory and search_text:
                item_name = str(row_data.get('item_name', '')).lower()
                category = str(row_data.get('category', '')).lower()
                if search_text.lower() not in item_name and search_text.lower() not in category:
                    continue

            row_idx = table.rowCount()
            table.insertRow(row_idx)
            if table == self.ui.table_recent:
                table.setItem(row_idx, 0, QTableWidgetItem(str(row_data['created_at'])))
                table.setItem(row_idx, 1, QTableWidgetItem(str(row_data['item_name'])))
                table.setItem(row_idx, 2, QTableWidgetItem(f"STOCK {row_data['movement_type']}"))
                table.setItem(row_idx, 3, QTableWidgetItem(str(row_data['quantity'])))
                table.setItem(row_idx, 4, QTableWidgetItem(str(row_data['FullName'])))
                table.setItem(row_idx, 5, QTableWidgetItem(str(row_data['notes'])))
            else:
                table.setItem(row_idx, 0, QTableWidgetItem(str(row_data['item_name'])))
                table.setItem(row_idx, 1, QTableWidgetItem(str(row_data['category'])))
                table.setItem(row_idx, 2, QTableWidgetItem(str(row_data['stock'])))
                table.setItem(row_idx, 3, QTableWidgetItem(str(row_data['min_stock'])))
                table.setItem(row_idx, 4, QTableWidgetItem(str(row_data['price'])))
                table.setItem(row_idx, 5, QTableWidgetItem(str(row_data['status'])))

    # -------- Search Inventory --------
    def on_search_inventory(self, text):
        self.fillTable(self.ui.table_inventory, staffM.currentinventory(), search_text=text)

    # -------- Populate ComboBoxes --------
    def populateComboBoxes(self):
        self.ui.combo_stockin_item.clear()
        self.ui.combo_stockout_item.clear()
        items = staffM.currentinventory()
        for item in items:
            self.ui.combo_stockin_item.addItem(item['item_name'])
            self.ui.combo_stockout_item.addItem(item['item_name'])

    # -------- Add New Item --------
    def addItem(self):
        item_name = self.ui.input_additem_name.text()
        category = self.ui.combo_additem_category.currentText()
        stock = self.ui.input_additem_stock.text()
        min_stock = self.ui.input_additem_minstock.text()
        price = self.ui.input_additem_price.text()

        # Validation
        if not item_name or not stock or not min_stock or not price:
            self.mes.show_warning(self, "Warning", "Please enter all the information")
            return
        if not stock.isdigit() or not min_stock.isdigit() or not price.replace('.', '', 1).isdigit():
            self.mes.show_warning(self, "Warning", "Stock, Min Stock, and Price must be numbers")
            return

        data = {
            'item_name': item_name,
            'category': category,
            'stock': int(stock),
            'min_stock': int(min_stock),
            'price': float(price)
        }

        if staffM.add_Item(data):
            self.mes.show_information(self, "Added Item","Successfully added item")
            self.ui.input_additem_name.setText("")
            self.ui.input_additem_stock.setText("")
            self.ui.input_additem_minstock.setText("")
            self.ui.input_additem_price.setText("")
            self.refresh()
            self.count()
            self.populateComboBoxes()
        else:
            self.mes.show_critical(self, "Error", "Failed to add item")

    # -------- Stock In --------
    def stockIn_tab(self):
        try:
            item_name = self.ui.combo_stockin_item.currentText()
            quantity = self.ui.input_stockin_qty.text()
            notes = self.ui.input_stockin_notes.toPlainText()

            if not item_name:
                self.mes.show_warning(self, "Warning", "Please select an item")
                return
            if not quantity.isdigit() or int(quantity) <= 0:
                self.mes.show_warning(self, "Warning", "Please enter a valid quantity")
                return
            quantity = int(quantity)

            product = staffM.stock_log(item_name)
            user = staffM.user(self.name)

            if not product:
                self.mes.show_critical(self, "Error", f"Item '{item_name}' not found in database")
                return
            if not user:
                self.mes.show_critical(self, "Error", f"User '{self.name}' not found in database")
                return

            data = {
                'product_id': product['product_id'],
                'user_id': user['user_id'],
                'quantity': quantity,
                'movement_type': 'IN',
                'reason': "Stocking more",
                'notes': notes
            }

            new_stock = int(product['stock']) + quantity

            if staffM.stockItem(data):
                staffM.stockupdate(new_stock, product['product_id'])
                self.mes.show_information(self, "Success", "Stocked In Item Successfully")
                self.ui.input_stockin_qty.setText("")
                self.ui.input_stockin_notes.clear()
                self.refresh()
                self.count()
            else:
                self.mes.show_critical(self, "Error", "Failed to record stock-in")

        except Exception as e:
            self.mes.show_critical(self, "Error", f"An error occurred:\n{str(e)}")

    # -------- Stock Out --------
    def stockOut_tab(self):
        try:
            item_name = self.ui.combo_stockout_item.currentText()
            quantity = self.ui.input_stockout_qty.text()
            reason = self.ui.combo_stockout_reason.currentText()
            notes = self.ui.input_stockout_notes.toPlainText()

            if not item_name:
                self.mes.show_warning(self, "Warning", "Please select an item")
                return
            if not quantity.isdigit() or int(quantity) <= 0:
                self.mes.show_warning(self, "Warning", "Please enter a valid quantity")
                return
            quantity = int(quantity)

            product = staffM.stock_log(item_name)
            user = staffM.user(self.name)

            if not product:
                self.mes.show_critical(self, "Error", f"Item '{item_name}' not found in database")
                return
            if not user:
                self.mes.show_critical(self, "Error", f"User '{self.name}' not found in database")
                return

            if int(product['stock']) < quantity:
                self.mes.show_warning(self, "Warning", "Not enough stock")
                return

            data = {
                'product_id': product['product_id'],
                'user_id': user['user_id'],
                'quantity': quantity,
                'movement_type': 'OUT',
                'reason': reason,
                'notes': notes
            }

            new_stock = int(product['stock']) - quantity

            if staffM.stockItem(data):
                staffM.stockupdate(new_stock, product['product_id'])
                self.mes.show_information(self, "Success", "Stocked Out Item Successfully")
                self.ui.input_stockout_qty.setText("")
                self.ui.input_stockout_notes.clear()
                self.refresh()
                self.count()
            else:
                self.mes.show_critical(self, "Error", "Failed to record stock-out")

        except Exception as e:
            self.mes.show_critical(self, "Error", f"An error occurred:\n{str(e)}")