#!/usr/bin/python3

import pymysql


def mysqlconnect():

    host = input("Enter your host: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    db_name= input("db name: ")
    conn = pymysql.connect(
        host = host,
        user = username,
        password = password,
        db = db_name,
        )
    cur =conn.cursor()
    choice =input("select_all/select_1/select_2/where/where_in:")
    if choice == "select_all":
        table_name = input("Enter your table name: ")
#    cur =conn.cursor()
#        cur =conn.cursor()
        cur.execute(f"select * from {table_name}")
        output = cur.fetchall()
        for i in output:
            print(i)
    elif choice == "select_1":
        fild_name = input("enter your field: ")
        table_name = input("Enter your table name: ")
#    cur =conn.cursor()
#        cur =conn.cursor()
        cur.execute(f"select {fild_name} from {table_name}")
        output = cur.fetchall()
        for i in output:
            print(i)
    elif choice == "select_2":
        fild_name_1 = input("enter your field first: ")
        fild_name_2 = input("enter your field second: ")
        table_name = input("Enter your table name: ")
#    cur =conn.cursor()
#        cur =conn.cursor()
        cur.execute(f"select {fild_name_1},{fild_name_2} from {table_name}")
        output = cur.fetchall()
        for i in output:
            print(i)
    elif choice == "where":
        fild_name_1 = input("enter your field first: ")
        fild_name_2 = input("enter your field second: ")
#        where= input("enter where: ")
        table_name = input("Enter your table name: ")
        where= input("enter where: ")

#    cur =conn.cursor()
#        cur =conn.cursor()
        cur.execute(f"select {fild_name_1},{fild_name_2} from {table_name} where {fild_name_1}={where}")
        output = cur.fetchall()
        for i in output:
            print(i)
    elif choice == "where_in":
        fild_name_1 = input("enter your field first: ")
        fild_name_2 = input("enter your field second: ")
#        where= input("enter where: ")
        table_name = input("Enter your table name: ")
        where= input("enter where: ")
        a = input("enter in ")
        b = input("enter in ")
        c = input("enter in ")
        d = input("enter in ")

#    cur =conn.cursor()
#        cur =conn.cursor()
        cur.execute(f"select {fild_name_1},{fild_name_2} from {table_name} where {where} in ({a},{b},{c},{d}) ")
        output = cur.fetchall()
        for i in output:
            print(i)


    conn.close()

if __name__ == "__main__":
    mysqlconnect()
