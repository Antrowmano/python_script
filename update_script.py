#!/usr/bin/python3

import pymysql
import time
import maskpass
import functools
def mysqlconnect():
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
    max_id=150
    min_query=("select min(id) from audit_activity where updated_at is null;")
    cur.execute(min_query)
    output = cur.fetchone()
    min_id = functools.reduce(lambda sub, ele: sub * 10 + ele, output)
    print(min_id)
    if min_id < max_id:
        for i in range(min_id,max_id,5):
            second_value=i+4
            query=(f"update audit_activity set updated_at=ADDTIME(created_at,3)where updated_at is null and id BETWEEN {i} and {second_value};")
            cur.execute(query)
            conn.commit()
            time.sleep(5)
#           print(f'Done {second_value}')
#        output = cur.fetchall()
#        for i in output:
#            print(i)


    conn.close()

if __name__ == "__main__":
    mysqlconnect()