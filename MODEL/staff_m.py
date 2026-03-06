import pymysql.cursors
from MODEL.database import db

class staffM:
    db_c = db()

    # -------count--------
    @staticmethod
    def totalItem():
        con = staffM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT COUNT(product_id) AS total FROM products")
                return cursor.fetchone()
        finally:
            con.close()

    @staticmethod
    def lowStock():
        con = staffM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT COUNT(product_id) AS total FROM products WHERE stock <= min_stock")
                return cursor.fetchone()
        finally:
            con.close()

    @staticmethod
    def getLowStockItems():
        con = staffM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("""
                    SELECT item_name, category, stock, min_stock 
                    FROM products 
                    WHERE stock <= min_stock
                    ORDER BY stock ASC
                """)
                return cursor.fetchall()
        finally:
            con.close()

    @staticmethod
    def stocks(stats):
        con = staffM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT COUNT(log_id) AS total FROM stock_logs WHERE movement_type=%s AND DATE(created_at) = CURDATE()", (stats,))
                return cursor.fetchone()
        finally:
            con.close()

    # -------table--------
    @staticmethod
    def recenttransaction():
        con = staffM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = """
                    SELECT s.created_at, s.movement_type, s.quantity, s.notes,
                           p.item_name, p.category, p.stock AS curstock, p.min_stock, p.price, p.status,
                           u.user_id, u.FullName
                    FROM stock_logs s
                    LEFT JOIN users u ON s.user_id = u.user_id
                    LEFT JOIN products p ON s.product_id = p.product_id
                """
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            con.close()

    @staticmethod
    def currentinventory():
        con = staffM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT * FROM products ORDER BY product_id DESC")
                return cursor.fetchall()
        finally:
            con.close()

    # ------id-----
    @staticmethod
    def stock_log(item_name):
        con = staffM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT * FROM products WHERE item_name = %s", (item_name,))
                return cursor.fetchone()
        finally:
            con.close()

    @staticmethod
    def user(name):
        con = staffM.db_c.connect()
        try:
            with con.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT * FROM users WHERE FullName = %s", (name,))
                return cursor.fetchone()
        finally:
            con.close()

    # ------insert-----
    @staticmethod
    def add_Item(data):
        con = staffM.db_c.connect()
        try:
            with con.cursor() as cursor:
                sql = """
                    INSERT INTO products
                        (item_name, category, stock, min_stock, price, status, created_at)
                    VALUES (%s, %s, %s, %s, %s, 'Available', CURRENT_TIMESTAMP)
                """
                cursor.execute(sql, (
                    data['item_name'], data['category'], int(data['stock']),
                    int(data['min_stock']), float(data['price'])
                ))
                con.commit()
                return True
        except Exception as e:
            print("Insert failed:", e)
            return False
        finally:
            con.close()

    @staticmethod
    def stockItem(data):
        con = staffM.db_c.connect()
        try:
            with con.cursor() as cursor:
                sql = """
                    INSERT INTO stock_logs
                        (product_id, user_id, quantity, movement_type, reason, notes, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
                """
                cursor.execute(sql, (
                    data['product_id'], data['user_id'], data['quantity'],
                    data['movement_type'], data['reason'], data['notes']
                ))
                con.commit()
                return True
        except Exception as e:
            print("Insert failed:", e)
            return False
        finally:
            con.close()

    @staticmethod
    def stockupdate(newstock, product_id):
        con = staffM.db_c.connect()
        try:
            with con.cursor() as cursor:
                cursor.execute("UPDATE products SET stock=%s WHERE product_id=%s", (newstock, product_id))
                con.commit()
        except Exception as e:
            print("Update failed:", e)
        finally:
            con.close()