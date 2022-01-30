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
    choice =input("enter your choice /create/alter: ")
    if choice == "create":
        create_table=input("create new table: ")
        cur.execute(f"{create_table}")
        table_name=input("show create table:")
        cur.execute(f"show create table {table_name}")
        output = cur.fetchall()
        print(output)
#        for i in output:
#            print(i)
    elif choice == "alter":
        choice =input("alter (add),(modify),(change),(index): ")
        if choice =="add":
            table_name=input("alter table (table_name): ")
            add =input("(add): ")
 #        add = input("for column(add), for modify(modify),for change(change)for index(add index): ")
            column_name=input("add (column_name): ")
            data_type=input("add (data_type): ")
            cur.execute(f"alter table {table_name} {add} {column_name} {data_type}")
            table_name=input("show create table: ")
            cur.execute(f"show create table {table_name}")
            output = cur.fetchall()
            print(output)
        elif choice == "modify":
            table_name=input("alter table (table_name): ")
            modify =input("(modify)")
            column_name=input("add (column_name): ")
            data_type=input("modify (data_type): ")
            cur.execute(f"alter table {table_name} {modify} {column_name} {data_type}")
            table_name=input("show create table: ")
            cur.execute(f"show create table {table_name}")
            output = cur.fetchall()
            print(output)
        elif choice == "change":
            table_name=input("alter table (table_name): ")
            old_name=input("(old_name): ")
            new_name=input("(new name): ")
#            column_name=input("add (column_name): ")
            data_type=input("modify (data_type): ")
            cur.execute(f"alter table {table_name} change {old_name} {new_name} {data_type}")
            table_name=input("show create table: ")
            cur.execute(f"show create table {table_name}")
            output = cur.fetchall()
            print(output)
        elif choice == "index":
            choice =input("(table_size): ")
            if choice == "table_size":
                table_name=input("enter table name: ")
                cur.execute("SELECT TABLE_NAME AS `Table`,ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024) AS `Size (MB)`FROM information_schema.TABLES WHERE TABLE_NAME ="'"{table_name}"'" ORDER BY(DATA_LENGTH + INDEX_LENGTH)DESC;")
                output = cur.fetchall()
                print(output)
                choice =input("without table lock(no)with table lock(yes): ")
                if choice == "no":
                    table_name=input("enter table name: ")
                    index_name=input("enter index name: ")
                    index_column=input("enter index column: ")
                    cur.execute(f"alter table {table_name} add index {index_name} ({index_column})")
#                    table_name=input("show create table: ")
                    cur.execute(f"show create table {table_name}")
                    output = cur.fetchall()
                    print(output)
                elif choice == "yes":
                    table_name=input("enter table name: ")
                    index_name=input("enter index name: ")
                    index_column=input("enter index column: ")
                    cur.execute(f"alter table {table_name} add index {index_name} ({index_column}), lock=none, algorithm=inplace")
#                    table_name=input("show create table: ")
                    cur.execute(f"show create table {table_name}")
                    output = cur.fetchall()
                    print(output)



#            table_name=input("alter table (table_name): ")
#            data_type=input("modify (data_type): ")
#            cur.execute(f"alter table {table_name} add index {index_name} ")
#            table_name=input("show create table: ")
#            cur.execute(f"show create table {table_name}")
#            output = cur.fetchall()
#            print(output)



        conn.close()

if __name__ == "__main__":
    mysqlconnect()
