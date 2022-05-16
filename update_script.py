!/opt/homebrew/bin/python3
# import sys
import pymysql
import time
import maskpass

def mysqlconnect():
    try:
        host = input("Enter your host: ")
        username = input("Enter your username: ")
        password = maskpass.askpass(prompt="Enter your password: ", mask="*")
        db_name= input("db name: ")
        conn = pymysql.connect(
            host = host,
            user = username,
            password = password,
            db = db_name,
            )
        cur =conn.cursor()
    #    min_id=1
        max_id=5433907
        min_query=("select min(id) from audit_activity where updated_at is null;")
        cur.execute(min_query)
        output = cur.fetchone()
        min_id = output[0]
        print(min_id)
        if min_id < max_id:
            for i in range(min_id,max_id,1000):
                second_value=i+999
                query=(f"update audit_activity set updated_at=ADDTIME(created_at,3) where updated_at is null and id BETWEEN {i} and {second_value};")
                print(query)
                cur.execute(query)
                conn.commit()
                time.sleep(0.3)

        conn.close()
    except Exception as E:
        print(E)

if __name__ == "__main__":
    mysqlconnect()