import cx_Oracle
import traceback
conn=None
try:
    conn=cx_Oracle.connect("mojo/mojo@127.0.0.1/xe")
    print("connected successfully to db")
    print("db version:", conn.version)
    print("username:", conn.username)
except cx_Oracle.DataError:
    print("sorry connection failed")
    print(traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("disconnected successfully")
