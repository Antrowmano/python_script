#!/usr/bin/python3

import pymysql
import yaml

def mysqlconnect():

#    host = input("Enter your host: ")
#    username = input("Enter your username: ")
#    password = input("Enter your password: ")
#    db_name= input("db name: ")
#    credentials = yaml.load(open('./cred.yml'))
#    username = credentials['database']['username']

    with open('cred.yml','r')as file:
        var = input("(server1)(server2): ")
        db = yaml.safe_load(file)
        host= (db[var]['hostname'])
        user= (db[var]['username'])
        password= (db[var]['password'])
#    db_name= input("db name: ")
    conn = pymysql.connect(
        host = host,
        user = user,
        password = password,
            )
    cur =conn.cursor()
    table_name=input("enter table_name): ")
    cur.execute(f"SELECT TABLE_NAME, TABLE_SCHEMA  FROM INFORMATION_SCHEMA.TABLES  WHERE TABLE_NAME like "'"{table_name}"'";")
    output = cur.fetchall()
    print(output)
#            table_name=input("show create table: ")
#            cur.execute(f"show create table {table_name}")
#            output = cur.fetchall()
#            print(output)



    conn.close()

if __name__ == "__main__":
    mysqlconnect()
