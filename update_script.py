#!/usr/bin/python3

import pymysql
import time
import maskpass

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
    min_id=1
    max_id=150

    for i in range(min_id,max_id,5):
        second_value=i+4
        query=(f"update employee_table set name = 'mano' where name ='antrow' and id BETWEEN {i} and {second_value};")
        cur.execute(query)
        conn.commit()
        time.sleep(3)
        print(f'Done {second_value}')
#        output = cur.fetchall()
#        for i in output:
#            print(i)

    conn.close()

if __name__ == "__main__":
    mysqlconnect()