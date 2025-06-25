import pyodbc
import os

db_path = r"C:\Users\LENOVO\Desktop\Dbase1\Database1.mdb"

if not os.path.exists(db_path):
    print("❌ Database file not found at:", db_path)
else:
    conn_str = (
        rf"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};"
        rf"DBQ={db_path};"
    )

    try:
        conn = pyodbc.connect(conn_str)
        print("✅ Connected to Access database!")
        conn.close()
    except Exception as e:
        print("❌ Connection failed:", e)

