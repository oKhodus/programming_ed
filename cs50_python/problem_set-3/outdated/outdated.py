def main():
    try:
        months = {
            "January": "1",
            "February": "2",
            "March": "3",
            "April": "4",
            "May": "5",
            "June": "6",
            "July": "7",
            "August": "8",
            "September" : "9",
            "October": "10",
            "November": "11",
            "December": "12"
        }
        inp = input("Date: ").strip()
        if "/" in inp:
            user_month, user_day, user_year = map(str, inp.split("/"))
        elif "," in inp:
            user_month, user_day, user_year = map(str, inp.replace(",", "").split(" "))
            if user_month in months:
                user_month = months[user_month]
            else:
                main()
        else:
            main()
        

        if int(user_month) > 12:
            main()
        if int(user_day) > 31:
            main()

        if int(user_day) < 10 and int(user_month) < 10:
                print(f"{user_year}-{"0"+user_month}-{"0"+user_day}")
        elif int(user_month) < 10:
            print(f"{user_year}-{"0"+user_month}-{user_day}")
        elif int(user_day) < 10:
            print(f"{user_year}-{user_month}-{"0"+user_day}")
        else:
            print(f"{user_year}-{user_month}-{user_day}")

    except ValueError:
        main()

if __name__ == "__main__":
    main()
