def nameNmail():
    print("Oleksii Khodus")
    print("exalchel@gmail.com")
nameNmail()


def greeting(name):
    print(f"Nice to meet you {name}")
greeting(input("Enter your name please: "))


def calc_area(leng, wid):
    calc = leng * wid
    print(f"Your area is {calc} (m^2)")

calc_area(float(input("Enter a length please (m): ")), 
float(input("Enter a width please (m): ")))

def calc_acres(leng, wid):
    acre = 43560
    calc = leng * wid

    acre_area = calc / acre
    print(f"\nYour area is {acre_area} (ac)")

calc_acres(float(input("Enter please length of garden (ft): ")),
float(input("Enter please width of garden (ft): ")))


def bottles(liter, great_liter):

    calc_less = liter * 0.1
    print(f"\nThe amount of bottles are: {liter}\nYou've received: $ {calc_less:.2f}")
    
    calc_great = great_liter * 0.25
    print(f"\nThe amount of bottles are: {great_liter}\nYou've received: $ {calc_great:.2f}")

    summary_bottles = sum((liter, great_liter))
    summary_received = sum((calc_less, calc_great))
    print(f"\nYour summary of bottles are: {summary_bottles}\nAll your summary of received is: $ {summary_received:.2f}")

bottles(int(input("Enter amount of bottle are less or equal to 1 (liter): ")),
int(input("Enter amount of bottles are greater than 1 (liter): ")))


def tips(sum_of_order):
    tax = sum_of_order * 0.2 
    # base tax in Estonia is 20 %
    tips = sum_of_order * 0.18

    summary = sum((sum_of_order, tax, tips)) 

    print(f"Tax (20%) for this order is: ${tax:.2f}\nTips (18%) for this order is: ${tips:.2f}\nSummary of all of this: ${summary:.2f}")

tips(float(input("Enter please a summary of your order (dollars): ")))

def summaryN(n):
    # summary = (n * (n + 1)) / 2
    summary = sum(range(1, n + 1))
    print(int(summary))
summaryN(int(input("Enter your number: ")))

def market(souvenirs, baubles):
    souvenirs *= 75
    baubles *= 112
    print(f"\nYour weight of souvenirs is: {souvenirs} grammes")
    print(f"\nYour weight of baubles is: {baubles} grammes")

    summary = sum((souvenirs, baubles))
    print(f"\nSummary of all packages is: {summary} grammes")

market(int(input("Amount of souvenirs: ")), int(input("Amount of baubles: ")))

def deposit(dep):
    # percent is 4%
    first_year = dep * 0.04
    dep1 = dep + first_year
    print(f"\nSummary for the first year is: $ {dep1:.2f}")


    second_year = dep1 * 0.04
    dep2 = dep1 + second_year
    print(f"\nSummary for the second year is: $ {dep2:.2f}")

    third_year = dep2 * 0.04
    dep3 = dep2 + third_year
    print(f"\nSummary for the third year is: $ {dep3:.2f}")

    total = sum((first_year, second_year, third_year))
    print(f"\nTotal sum of percent of deposit is: $ {total:.2f}")


deposit(float(input("Enter your amount of deposit (dollars): $ ")))




