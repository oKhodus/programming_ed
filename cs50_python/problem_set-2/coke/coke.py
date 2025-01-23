def main():
    base_amount = 50
    str_amount = "Amount Due: "
    preffered_cents = [25, 10, 5]

    while base_amount > 0:
        print(f"{str_amount}{base_amount}")
        user_inp = int(input("Insert Coin: "))
        if user_inp in preffered_cents:
            base_amount -= user_inp
        else:
            print("Your input of cents is incorrect, please enter only 25, 10 or 5 cents.")

    if base_amount < 0:
         print(f"Change Owed: {-base_amount}")
    else:
        print("Change Owed: 0")

main()
