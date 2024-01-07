import csv
import datetime as dt
import subprocess as sp
import sys

def module_installed(module_name):
    try:
        __import__(module_name)
        return True
    except:
        return False

if module_installed("prettytable") == False:
    ask = input("The module prettytable is not installed. Do you want to install it? y/n ")
    if ask == "y":
        print("Installing the module please wait...")
        sp.run("pip install prettytable", shell=True,stdout=sp.DEVNULL, stderr=sp.DEVNULL,)
        print("The module prettytable has been installed...")
    else:
        print("\nError: The 'haircut_manager' module cannot function properly without the 'prettytable' module.")
        print("To continue, please install the required module by running the following command:")
        print("\tpip install prettytables")
        print("Or, please run the program again and press 'y' when prompted to install 'prettytables' module.")
        print("After installation, you can run the 'haircut_manager' module again.")
        sys.exit("Terminating the program...")

import prettytable as pt

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
    table = pt.PrettyTable()
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

def date_reformat(date):
    day,month,year = map(int, date.split("-"))
    return dt.datetime(year,month,day)

def last_date():
    max = date_reformat(records[0][0])
    for date in records:
        current = date_reformat(date[0])
        if current>max:
            max = current
    return max

def days_since_last_haircut(cd):
    duration = last_date() - cd
    days = duration.days

    if days > 30:
        return f"{days//30} month {days - ((days//30) * 30 )}days"
    else:
        return days