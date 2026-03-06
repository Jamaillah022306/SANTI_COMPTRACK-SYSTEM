from datetime import datetime, date

from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog, QAbstractItemView
from PyQt6.QtCore import QDate
from VIEW.admin_v import Ui_AdminDashboard
from VIEW.message import Ui_message
from MODEL.admin_m import adminM


class admin(QMainWindow):
    def __init__(self, manager=None, name=""):
        super().__init__()
        self.ui = Ui_AdminDashboard()
        self.mes = Ui_message()
        self.ui.setupUi(self)
        self.manager = manager

        # Connect signals
        self.ui.btn_logout.clicked.connect(self.logout)
        self.ui.btn_filter.clicked.connect(self.filter_history)
        self.ui.btn_export.clicked.connect(self.export_to_pdf)
        self.ui.search_inventory.textChanged.connect(self.search_inventory)

        self.ui.label_user.setText(f"Welcome, {name}")

        # Set default date range: 2024-01-01 to today
        self.ui.date_from.setDate(QDate(2024, 1, 1))
        self.ui.date_to.setDate(QDate.currentDate())

        # Disable table editing
        self.ui.table_history.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.table_inventory.setEditTriggers(QAbstractItem .EditTrigger.NoEditTriggers)

        # Initial load
        self.load_dashboard()
        self.load_inventory()
        self.filter_history()

    # ─────────────────────────── HELPERS ────────────────────────────────────

    @staticmethod
    def _fmt_date(value) -> str:
        """Safely convert any date/datetime/string to a readable string."""
        if value is None:
            return ""
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(value, date):
            return value.strftime("%Y-%m-%d")
        return str(value)

    # ─────────────────────────── NAVIGATION ─────────────────────────────────

    def logout(self):
        if self.manager:
            self.manager.show_login()

    # ─────────────────────────── DASHBOARD TAB ──────────────────────────────

    def load_dashboard(self):
        """Load summary cards and draw charts on the Analytics Dashboard tab."""
        # ── Summary cards ──
        total    = adminM.totalItem()
        lowstock = adminM.lowStock()
        stock_in = adminM.stocks("IN")
        stock_out= adminM.stocks("OUT")

        self.ui.lbl_card_total_v.setText(str(total.get("total", 0) if total else 0))
        self.ui.lbl_card_lowstock_v.setText(str(lowstock.get("total", 0) if lowstock else 0))
        self.ui.lbl_card_stockin_v.setText(str(stock_in.get("total", 0) if stock_in else 0))
        self.ui.lbl_card_stockout_v.setText(str(stock_out.get("total", 0) if stock_out else 0))

        # ── Analytics charts ──
        per_item, overall = adminM.getAnalyticsData()

        # Bar chart
        bar_fig = self.ui.bar_fig
        bar_fig.clear()
        ax = bar_fig.add_subplot(111)

        if per_item:
            labels   = [r["item_name"] for r in per_item]
            in_vals  = [r["total_in"]  for r in per_item]
            out_vals = [r["total_out"] for r in per_item]

            # Abbreviate long names
            short_labels = [lbl[:18] + "…" if len(lbl) > 18 else lbl for lbl in labels]

            import numpy as np
            x = np.arange(len(short_labels))
            w = 0.35
            bars_in  = ax.bar(x - w/2, in_vals,  w, label="Stock In",  color="#2ECC71", edgecolor="white")
            bars_out = ax.bar(x + w/2, out_vals, w, label="Stock Out", color="#E74C3C", edgecolor="white")

            ax.set_xticks(x)
            ax.set_xticklabels(short_labels, rotation=30, ha="right", fontsize=7)
            ax.set_ylabel("Quantity", fontsize=9)
            ax.set_title("Stock In vs Stock Out per Item (Top 10)", fontsize=10, fontweight="bold", color="#2C3E50")
            ax.legend(fontsize=8)
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.yaxis.grid(True, linestyle="--", alpha=0.5)
            ax.set_axisbelow(True)
        else:
            ax.text(0.5, 0.5, "No transaction data available",
                    ha="center", va="center", transform=ax.transAxes, fontsize=10, color="gray")
            ax.axis("off")

        bar_fig.tight_layout(pad=1.5)
        self.ui.bar_canvas.draw()

        # Pie chart
        pie_fig = self.ui.pie_fig
        pie_fig.clear()
        ax2 = pie_fig.add_subplot(111)

        total_in  = int(overall.get("overall_in",  0) or 0) if overall else 0
        total_out = int(overall.get("overall_out", 0) or 0) if overall else 0

        if total_in + total_out > 0:
            wedge_colors = ["#2ECC71", "#E74C3C"]
            wedges, texts, autotexts = ax2.pie(
                [total_in, total_out],
                labels=None,
                autopct="%1.1f%%",
                colors=wedge_colors,
                startangle=90,
                pctdistance=0.6,
                wedgeprops={"edgecolor": "white", "linewidth": 2},
            )
            for at in autotexts:
                at.set_fontsize(10)
                at.set_color("white")
                at.set_fontweight("bold")
            ax2.legend(
                wedges,
                [f"Stock In ({total_in})", f"Stock Out ({total_out})"],
                loc="lower center",
                bbox_to_anchor=(0.5, -0.08),
                fontsize=9,
                frameon=False,
            )
            ax2.set_title("Overall Distribution", fontsize=11, fontweight="bold", color="#2C3E50", pad=10)
        else:
            ax2.text(0.5, 0.5, "No data", ha="center", va="center",
                     transform=ax2.transAxes, fontsize=10, color="gray")
            ax2.axis("off")

        pie_fig.tight_layout(rect=[0, 0, 1, 0.93])
        self.ui.pie_canvas.draw()

    # ─────────────────────────── INVENTORY TAB ──────────────────────────────

    def load_inventory(self, search_text=""):
        """Fetch inventory from model and populate the inventory table."""
        data = adminM.getInventory()
        table = self.ui.table_inventory
        table.setSortingEnabled(False)   # disable while filling to avoid sort glitches
        table.setRowCount(0)

        for item in data:
            item_name = str(item.get("item_name", ""))
            category  = str(item.get("category", ""))

            if search_text and (
                search_text.lower() not in item_name.lower()
                and search_text.lower() not in category.lower()
            ):
                continue

            r = table.rowCount()
            table.insertRow(r)
            table.setItem(r, 0, QTableWidgetItem(item_name))
            table.setItem(r, 1, QTableWidgetItem(category))
            table.setItem(r, 2, QTableWidgetItem(str(item.get("current_stock", ""))))
            table.setItem(r, 3, QTableWidgetItem(str(item.get("min_stock", ""))))
            table.setItem(r, 4, QTableWidgetItem(str(item.get("price", ""))))
            table.setItem(r, 5, QTableWidgetItem(str(item.get("status", ""))))

        table.setSortingEnabled(True)

    def search_inventory(self, text):
        self.load_inventory(search_text=text)

    # ─────────────────────────── HISTORY TAB ────────────────────────────────

    def filter_history(self):
        """Fetch filtered transaction history from model and populate the table."""
        dfrom = self.ui.date_from.date().toPyDate().strftime("%Y-%m-%d")
        dto   = self.ui.date_to.date().toPyDate().strftime("%Y-%m-%d")

        if dfrom > dto:
            self.mes.show_warning(self, "Invalid Date Range",
                                  "From date cannot be later than To date.")
            return

        data = adminM.recenttransaction(dfrom, dto)
        self._populate_history_table(data)

    def _populate_history_table(self, data):
        """Fill the history table from a list of dicts returned by the model."""
        table = self.ui.table_history
        table.setSortingEnabled(False)
        table.setRowCount(0)

        if not data:
            table.setSortingEnabled(True)
            return

        for row, p in enumerate(data):
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(str(p.get("log_id", ""))))
            table.setItem(row, 1, QTableWidgetItem(self._fmt_date(p.get("created_at"))))
            table.setItem(row, 2, QTableWidgetItem(str(p.get("item_name", ""))))
            table.setItem(row, 3, QTableWidgetItem(f"STOCK {p.get('movement_type', '')}"))
            table.setItem(row, 4, QTableWidgetItem(str(p.get("quantity", ""))))
            table.setItem(row, 5, QTableWidgetItem(str(p.get("stock", ""))))
            table.setItem(row, 6, QTableWidgetItem(str(p.get("FullName", ""))))

        table.setSortingEnabled(True)

    # ─────────────────────────── EXPORT PDF ─────────────────────────────────

    def export_to_pdf(self):
        dfrom = self.ui.date_from.date().toPyDate().strftime("%Y-%m-%d")
        dto   = self.ui.date_to.date().toPyDate().strftime("%Y-%m-%d")

        if dfrom > dto:
            self.mes.show_warning(self, "Invalid Date Range",
                                  "From date cannot be later than To date.")
            return

        default_name = f"transaction_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export Transaction History", default_name, "PDF Files (*.pdf)"
        )
        if not file_path:
            return

        try:
            from reportlab.lib.pagesizes import landscape, A4
            from reportlab.lib import colors
            from reportlab.lib.units import cm
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.enums import TA_LEFT, TA_CENTER

            data = adminM.recenttransaction(dfrom, dto)
            if not data:
                self.mes.show_warning(self, "No Data",
                                      "There are no transactions for the selected date range.")
                return

            doc = SimpleDocTemplate(
                file_path, pagesize=landscape(A4),
                rightMargin=1.5*cm, leftMargin=1.5*cm,
                topMargin=1.5*cm, bottomMargin=1.5*cm
            )
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle("Title", parent=styles["Normal"],
                fontSize=16, fontName="Helvetica-Bold",
                textColor=colors.HexColor("#2C3E50"), spaceAfter=6, alignment=TA_CENTER)
            sub_style = ParagraphStyle("Sub", parent=styles["Normal"],
                fontSize=10, fontName="Helvetica-Bold",
                textColor=colors.HexColor("#2C3E50"), spaceAfter=4, alignment=TA_CENTER)
            info_style = ParagraphStyle("Info", parent=styles["Normal"],
                fontSize=9, fontName="Helvetica",
                textColor=colors.HexColor("#2C3E50"), spaceAfter=12, alignment=TA_CENTER)

            elements = []
            elements.append(Paragraph("COMPUTER INVENTORY", title_style))
            elements.append(Paragraph("Stock History Report", sub_style))
            elements.append(Paragraph(f"Period: {dfrom} to {dto}", info_style))
            gen_time = datetime.now().strftime("%B %d, %Y %I:%M %p")
            name_text = self.ui.label_user.text().replace("Welcome, ", "")
            elements.append(Paragraph(f"Generated by: {name_text} | {gen_time}", info_style))
            elements.append(Spacer(1, 0.4*cm))

            # ── Summary ──
            total_records = len(data)
            txn_in  = sum(1 for p in data if p.get("movement_type") == "IN")
            txn_out = sum(1 for p in data if p.get("movement_type") == "OUT")

            summary_data = [
                ["Total Transactions", "Stock IN", "Stock OUT"],
                [str(total_records), str(txn_in), str(txn_out)],
            ]
            summary_table = Table(summary_data, colWidths=[7.43*cm, 7.43*cm, 7.44*cm])
            summary_style = TableStyle([
                ("BACKGROUND", (0,0), (0,0), colors.HexColor("#2C3E50")),
                ("BACKGROUND", (1,0), (1,0), colors.HexColor("#27AE60")),
                ("BACKGROUND", (2,0), (2,0), colors.HexColor("#E74C3C")),
                ("TEXTCOLOR", (0,0), (-1,0), colors.white),
                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
                ("FONTSIZE", (0,0), (-1,0), 9),
                ("ALIGN", (0,0), (-1,-1), "CENTER"),
                ("TOPPADDING", (0,0), (-1,0), 8),
                ("BOTTOMPADDING", (0,0), (-1,0), 8),
                ("BACKGROUND", (0,1), (-1,1), colors.HexColor("#F8F9FA")),
                ("FONTNAME", (0,1), (-1,1), "Helvetica-Bold"),
                ("FONTSIZE", (0,1), (-1,1), 22),
                ("TEXTCOLOR", (0,1), (0,1), colors.HexColor("#2C3E50")),
                ("TEXTCOLOR", (1,1), (1,1), colors.HexColor("#27AE60")),
                ("TEXTCOLOR", (2,1), (2,1), colors.HexColor("#E74C3C")),
                ("TOPPADDING", (0,1), (-1,1), 4),
                ("BOTTOMPADDING", (0,1), (-1,1), 20),
                ("BOX", (0,0), (0,-1), 1, colors.HexColor("#2C3E50")),
                ("BOX", (1,0), (1,-1), 1, colors.HexColor("#27AE60")),
                ("BOX", (2,0), (2,-1), 1, colors.HexColor("#E74C3C")),
            ])
            summary_table.setStyle(summary_style)
            elements.append(summary_table)
            elements.append(Spacer(1, 0.5*cm))

            headers = ["TXN ID", "Date & Time", "Item Name", "Type", "Qty", "Stock"]
            col_widths = [1.5*cm, 4.5*cm, 10*cm, 3*cm, 1.5*cm, 1.8*cm]
            table_data = [headers]
            for p in data:
                fmt_date = p.get("created_at").strftime("%b %d, %Y %I:%M %p") if p.get("created_at") else ""
                table_data.append([
                    str(p.get("log_id", "")), fmt_date, str(p.get("item_name", "")),
                    "STOCK " + str(p.get("movement_type", "")), str(p.get("quantity", "")),
                    str(p.get("stock", "")),
                ])

            t = Table(table_data, colWidths=col_widths, repeatRows=1)
            ts = TableStyle([
                ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#2C3E50")),
                ("TEXTCOLOR", (0,0), (-1,0), colors.white),
                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
                ("FONTSIZE", (0,0), (-1,0), 9),
                ("ALIGN", (0,0), (-1,0), "CENTER"),
                ("BOTTOMPADDING", (0,0), (-1,0), 8),
                ("TOPPADDING", (0,0), (-1,0), 8),
                ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
                ("FONTSIZE", (0,1), (-1,-1), 8),
                ("TEXTCOLOR", (0,1), (-1,-1), colors.HexColor("#2C3E50")),
                ("ALIGN", (0,1), (-1,-1), "CENTER"),
                ("ALIGN", (2,1), (2,-1), "LEFT"),
                ("BOTTOMPADDING", (0,1), (-1,-1), 6),
                ("TOPPADDING", (0,1), (-1,-1), 6),
                ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#ECF0F1")]),
                ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#BDC3C7")),
                ("LINEBELOW", (0,0), (-1,0), 1.5, colors.HexColor("#2C3E50")),
            ])
            for i, p in enumerate(data, start=1):
                c = colors.HexColor("#27AE60") if p.get("movement_type","") == "IN" else colors.HexColor("#E74C3C")
                ts.add("TEXTCOLOR", (3,i), (3,i), c)
                ts.add("FONTNAME", (3,i), (3,i), "Helvetica-Bold")
            t.setStyle(ts)
            elements.append(t)
            doc.build(elements)

            self.mes.show_information(self, "Export Successful",
                f"Exported {len(data)} record(s) to:\n{file_path}")

        except ImportError:
            self.mes.show_critical(self, "Missing Library",
                "reportlab is not installed.\nPlease run:\npip install reportlab")
        except Exception as e:
            self.mes.show_critical(self, "Export Failed", f"An error occurred:\n{str(e)}")