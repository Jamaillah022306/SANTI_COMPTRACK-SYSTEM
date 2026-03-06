import pymysql.cursors
import bcrypt


class db:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.db = "inventory_system"
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db  # Fixed key to 'database'
            )
            return self.connection
        except Exception as e:
            print(f"Connection Error: {e}")
            return None

    def result(self, username, password):
        connection = self.connect()
        if not connection:
            return None

        found_user = None
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                # 1. Look for the user by username ONLY
                # Note: table name 'users' and column 'user_id' as requested
                sql = "SELECT * FROM users WHERE username = %s"
                cursor.execute(sql, (username,))
                found_user = cursor.fetchone()

            # 2. Check if user exists and verify the hash
            if found_user:
                stored_hash = found_user.get('PasswordHash')

                # bcrypt.checkpw requires bytes
                provided_password = password.encode('utf-8')
                hashed_password = stored_hash.encode('utf-8')

                if bcrypt.checkpw(provided_password, hashed_password):
                    # Password matches! Return the user dictionary
                    return found_user
                else:
                    # Password doesn't match
                    print("Debug: Password mismatch.")
                    return None

            return None  # User not found

        except Exception as e:
            print(f"Query Error: {e}")
            return None

        finally:
            if connection:
                connection.close()