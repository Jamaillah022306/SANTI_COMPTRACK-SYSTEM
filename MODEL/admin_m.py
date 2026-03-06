import pymysql.cursors
from MODEL.database import db

class adminM:
    db_c = db()


    # -------count--------
    @staticmethod
    def totalItem():
        con = adminM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = """SELECT COUNT(product_id) AS total FROM products"""
                cursor.execute(sql)
                return cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            if con:
                con.close()

    @staticmethod
    def lowStock():
        con = adminM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = """SELECT COUNT(product_id) AS total FROM products
                        WHERE stock <= min_stock"""
                cursor.execute(sql)
                return cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            if con:
                con.close()

    @staticmethod
    def stocks(stats):
        con = adminM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = """SELECT COALESCE(SUM(quantity), 0) AS total FROM stock_logs
                        WHERE movement_type = %s"""
                cursor.execute(sql, (stats,))
                return cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            if con:
                con.close()

    # -------table--------

    @staticmethod
    def recenttransaction(fromdate, todate):
        con = adminM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = """SELECT s.created_at, s.movement_type, s.quantity, s.notes, s.log_id,
                                p.item_name, p.category, p.stock, p.min_stock, p.price, p.status,
                                u.user_id, u.FullName
                        FROM stock_logs s
                        LEFT JOIN users u ON s.user_id = u.user_id
                        LEFT JOIN products p ON s.product_id = p.product_id
                        WHERE s.created_at BETWEEN %s AND %s"""
                cursor.execute(sql, (fromdate, todate,))
                return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            if con:
                con.close()

    @staticmethod
    def getInventory():
        con = adminM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = """SELECT item_name, category, stock AS current_stock, 
                                min_stock, price, status 
                         FROM products
                         ORDER BY item_name ASC"""
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            if con:
                con.close()

    @staticmethod
    def getAnalyticsData():
        """Returns per-item stock in/out totals and overall summary."""
        con = adminM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                # Per-item totals
                sql_items = """
                    SELECT item_name, total_in, total_out
                    FROM (
                        SELECT p.item_name,
                               SUM(CASE WHEN s.movement_type = 'IN'  THEN s.quantity ELSE 0 END) AS total_in,
                               SUM(CASE WHEN s.movement_type = 'OUT' THEN s.quantity ELSE 0 END) AS total_out
                        FROM stock_logs s
                        LEFT JOIN products p ON s.product_id = p.product_id
                        GROUP BY p.product_id, p.item_name
                    ) AS item_totals
                    ORDER BY (total_in + total_out) DESC
                    LIMIT 10
                """
                cursor.execute(sql_items)
                per_item = cursor.fetchall()

                # Overall totals
                sql_overall = """
                    SELECT
                        SUM(CASE WHEN movement_type = 'IN'  THEN quantity ELSE 0 END) AS overall_in,
                        SUM(CASE WHEN movement_type = 'OUT' THEN quantity ELSE 0 END) AS overall_out
                    FROM stock_logs
                """
                cursor.execute(sql_overall)
                overall = cursor.fetchone()
                return per_item, overall
        except Exception as e:
            print(e)
            return [], {}
        finally:
            if con:
                con.close()