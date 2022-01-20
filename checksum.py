#!/usr/bin/python3

import schedule
import time




file_1 = open("test.txt", "r")

file_r1=file_1.read()



def job():
    file_2 = open("test.txt", "r")
    file_r2=file_2.read()

    if  file_r1 == file_r2:
        print('Equal')
    else:
        print('Not Equal')


schedule.every(60).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
