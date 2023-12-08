import csv
import datetime as dt
from prettytable import *


records = []
temp_records = []

def one_liner(cd):
    final_lst = []
    tday_tmrw = input("Did you cut you hair today y/n ")
    if tday_tmrw == "y":
        date_str = f"{cd.day}-{cd.month}-{cd.year}"
        weekday = cd.strftime("%A")
    else:
        dm = int(input("what date of month was it? "))
        while dm > cd.day:
            print("It's not possible choose a date in future. ")
            dm = int(input("what date of month was it? "))
        new_cd = dt.date(cd.year,cd.month,dm)
        date_str = f"{new_cd.day}-{new_cd.month}-{new_cd.year}"
        weekday = new_cd.strftime("%A")
    askplace = input("where did you cut your hair from ")
    cost = input("How much did it cost? ")
    final_lst += [date_str,askplace,cost,weekday]
    final_str = ",".join(final_lst)
    return f"\n{final_str}"

def load_data():
    global records
    with open("log.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row == ['Date', 'Place', 'Cost', 'Weekday']:
                pass
            elif row not in records:
                records += [row]
        print("Records loaded...")

def show_data():
    load_data()
    table = PrettyTable()
    table.field_names=["No.","Date","Place","Cost","Weekday"]
    for i in range(len(records)):
        table.add_row([f"{i+1}",f"{records[i][0]}",f"{records[i][1]}",f"{records[i][2]}",f"{records[i][3]}"])
    print(table)

def delete_from_records(turn):
    global temp_records,records
    for index, lines in enumerate(records):
        if index not in range(turn, len(records) + 1):
            temp_records += [lines]
    records = temp_records
    temp_records = []

def delete_untill_records(turn):
    global temp_records,records
    for index, lines in enumerate(records):
        if index not in range(0,turn):
            temp_records += [lines]
    records = temp_records
    temp_records = []

def reconstruct_csv():
    with open("log.csv", "w") as file:
        file.write("Date,Place,Cost,Weekday")
        for record in records:
            updated_str = ",".join(record)
            file.write(f"\n{updated_str}")
        file.close()