import pymysql
import bcrypt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'inventory_system'
}

def update_all_passwords():
    connection = None
    try:
        # 1. Connect to the database
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # 2. Fetch all users (Updated query: user_id and users)
        cursor.execute("SELECT user_id, PasswordHash FROM users")
        users_list = cursor.fetchall()

        print(f"--- Starting update for {len(users_list)} users ---")

        for user in users_list:
            u_id = user['user_id'] # Updated key
            plain_text = user['PasswordHash']

            # Skip if it's already a bcrypt hash
            if plain_text.startswith('$2'):
                print(f"Skipping user_id {u_id}: Already hashed.")
                continue

            # 3. Generate the new hash
            hashed = bcrypt.hashpw(plain_text.encode('utf-8'), bcrypt.gensalt())
            hash_string = hashed.decode('utf-8')

            # 4. Update the database (Updated query: users and user_id)
            update_sql = "UPDATE users SET PasswordHash = %s WHERE user_id = %s"
            cursor.execute(update_sql, (hash_string, u_id))

            print(f"✅ user_id {u_id}: Updated plain-text to hash.")

        # 5. Commit changes
        connection.commit()
        print("\n--- All updates committed successfully! ---")

    except Exception as e:
        print(f"❌ Error during update: {e}")
    finally:
        if connection:
            connection.close()

# Fixed the typo here: changed _main_ to __main__
if __name__ == "__main__":
    update_all_passwords()