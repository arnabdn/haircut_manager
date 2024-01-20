import datetime as dt
import functions as fn

cd = dt.datetime.now()

records = fn.records

fn.load_data()
fn.update_places()


while True:
    user_op = input("\n" +
    "+-----------------------+\n" +
    "|      Main Menu        |\n" +
    "| What would you like   |\n" +
    "| to do?                |\n" +
    "| 1. Add data           |\n" +
    "| 2. Reset data         |\n" +
    "| 3. See stats          |\n" +
    "| 4. Quit               |\n" +
    "+-----------------------+\n")

    if user_op == "1":
        with open("log.csv","a") as file:
                line = fn.one_liner(cd)
                file.write(line)
                file.close()
                fn.load_data()
                fn.update_places() 
                continue     
    elif user_op == "2":
        ops = input("Do you want to delete all the data? y/n ")
        if ops == "y":
            with open("log.csv","w") as file:
                file.write("Date,Place,Cost,Weekday")
                file.close()
            fn.records = []

        elif ops == "n":
            if len(records) > 0:
                while True:
                    option = input("you have two options:\n"
                        "1. Reset data starting from a date\n"
                        "2. Reset data untill a date\n")
                    if option == "1":
                        fn.show_data()
                        turn = int(input("starting from(exclusive) which entry you want to reset data? answer in numbers\n"))
                        fn.delete_from_records(turn)
                        fn.reconstruct_csv()
                        fn.update_places()
                    if option == "2":
                        fn.show_data()
                        turn = int(input("up until(inclusive) which entry you want to reset data? anwer in numbers\n"))
                        fn.delete_untill_records(turn)
                        fn.reconstruct_csv()
                        fn.update_places()
                    op = input("Do you want to reset more entry? y/n\n")
                    if op == "y":
                        continue
                    else:
                        break
            else:
                print("Records are Empty opereation is unavailable")
            
    elif user_op == "3":
        print(f"Days Since Last Haircut:                    {fn.days_since_last_haircut(cd)}")
        print(f"Total Haircuts This Year:                   {fn.yearly_haircut(cd)}")
        print(f"Haircuts Per Month This Year:               {fn.monthly_haircut_currentyear(cd)}")
        print(f"Haircuts Per Month Since Start of Records:  {fn.overall_monthly_haircut(cd)}")
        print(f"Total Cost This Year:                       \u09F3{fn.total_cost_current_year(cd)}")
        print(f"Total Cost Since Start of Records:          \u09F3{fn.total_cost()}")
        print(f"Places with the Most Haircuts:              {fn.most_haircut()}")
    
    elif user_op == "4":
        print("See you next time!")
        break
    else:
        print("Invalid option")