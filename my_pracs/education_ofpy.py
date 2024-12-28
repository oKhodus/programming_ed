# Made by Oleksii (Lex) Khodus 
# My github - https://github.com/oKhodus
# Exercises from "The Python Workbook: A Brief Introduction with Exercises
# and Solutions. by Ben Stephensons"
# 
#            __    __  __                        __                     
#           /  |  /  |/  |                      /  |                    
#   ______  $$ | /$$/ $$ |____    ______    ____$$ | __    __   _______ 
#  /      \ $$ |/$$/  $$      \  /      \  /    $$ |/  |  /  | /       |
# /$$$$$$  |$$  $$<   $$$$$$$  |/$$$$$$  |/$$$$$$$ |$$ |  $$ |/$$$$$$$/ 
# $$ |  $$ |$$$$$  \  $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$      \ 
# $$ \__$$ |$$ |$$  \ $$ |  $$ |$$ \__$$ |$$ \__$$ |$$ \__$$ | $$$$$$  |
# $$    $$/ $$ | $$  |$$ |  $$ |$$    $$/ $$    $$ |$$    $$/ /     $$/ 
#  $$$$$$/  $$/   $$/ $$/   $$/  $$$$$$/   $$$$$$$/  $$$$$$/  $$$$$$$/  
                                                                      
                                                                      
                                                    
# Chapter ^1
import math
import time
# Exercise ^1
def task1():
    print("Oleksii Khodus")
    print("hello@yahoo.com")

# Exercise ^2
def task2():
    name = input("Enter your name please: ")
    print(f"Nice to meet you {name}")

# Exercise ^3
def task3():
    leng = float(input("Enter a length please (m): "))
    wid = float(input("Enter a width please (m): "))
    calc = leng * wid
    print(f"Your area is {int(calc)} (m^2)")

# Exercise ^4
def task4():
    leng = float(input("Enter please length of garden (ft): "))
    wid = float(input("Enter please width of garden (ft): "))
    acre = 43560
    calc = leng * wid

    acre_area = calc / acre
    print(f"\nYour area is {acre_area} (ac)")

# Exercise ^5
def task5():
    liter = int(input("Enter amount of bottle are less or equal to 1 (liter): "))
    great_liter = int(input("Enter amount of bottles are greater than 1 (liter): "))
    calc_less = liter * 0.1
    print(f"\nThe amount of bottles are: {liter}\nYou've received: $ {calc_less:.2f}")
    
    calc_great = great_liter * 0.25
    print(f"\nThe amount of bottles are: {great_liter}\nYou've received: $ {calc_great:.2f}")

    summary_bottles = sum((liter, great_liter))
    summary_received = sum((calc_less, calc_great))
    print(f"\nYour summary of bottles are: {summary_bottles}\nAll your summary of received is: $ {summary_received:.2f}")

# Exercise ^6
def task6():
    sum_of_order = float(input("Enter please a summary of your order (dollars): "))
    tax = sum_of_order * 0.2 
    # base tax in Estonia is 20 %
    tips = sum_of_order * 0.18

    summary = sum((sum_of_order, tax, tips)) 

    print(f"\nTax (20%) for this order is: ${tax:.2f} \
    \nTips (18%) for this order is: ${tips:.2f} \
    \nSummary of all of this: ${summary:.2f}")

# Exercise ^7
def task7():
    n = int(input("Enter your number: "))
    # summary = (n * (n + 1)) / 2
    summary = sum(range(1, n + 1))
    print(int(summary))

# Exercise ^8
def task8():
    souvenirs = int(input("Amount of souvenirs: "))
    baubles = int(input("Amount of baubles: "))
    souvenirs *= 75
    baubles *= 112
    print(f"\nYour weight of souvenirs is: {souvenirs} grammes")
    print(f"\nYour weight of baubles is: {baubles} grammes")

    summary = sum((souvenirs, baubles))
    print(f"\nSummary of all packages is: {summary} grammes")

# Exercise ^9
def task9():
    dep = float(input("Enter your amount of deposit (dollars): $ "))
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

# Exercise ^10
def task10():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    sumof = a + b
    minused = a - b
    multiply = a * b
    part = a / b
    log10 = math.log10(a)
    sqrtB = a ** b

    print(f"\n Summary is: {sumof}")
    print(f"\n Minused is: {minused}")
    print(f"\n Multiply of a and b is: {multiply}")
    print(f"\n Part of a and b is: {part}")
    print(f"\n Log10 of a is: {log10}")
    print(f"\n Square of a in b is: {sqrtB}")

# Exercise ^11
def task11():
    fuel = float(input("Enter how much MPG (miles-per-gallon) fuel your car uses: "))
    L100km = (282.48 / fuel)
    print(f"In Canada you'll have {L100km:.2f} L/100 km.") 

# Exercise ^12
def task12():
    str_lat = "Enter a coordinate for the {} object latitude ({}): "
    str_long = "Enter a coordinate for the {} object longitude ({}): "

    w1 = float(input(str_lat.format("first","w1")))
    h1 = float(input(str_long.format("first","h1")))
    w2 = float(input(str_lat.format("second","w2")))
    h2 = float(input(str_long.format("second","h2")))


    w1 = math.radians(w1)
    w2 = math.radians(w2)
    h1 = math.radians(h1)
    h2 = math.radians(h2)

    dist = 6371.01 * math.acos(
        math.sin(w1) * math.sin(w2) + math.cos(w1) * math.cos(w2) * math.cos(h1 - h2)
    )
    print(f"\nMost short distance between these two coordinates is: {dist:.2f} km")

# Exercise ^13
def task13():
    cents = int(input("Enter a value of cents: ¢ "))
    bucks_2 = 200
    buck = 100
    cents_25 = 25
    cents_10 = 10
    cents_5 = 5
    cent_1 = 1

    print(f"\nYou need {cents // bucks_2} dollar(s), with nominale of: $ {bucks_2 // 100} bucks")
    cents %= bucks_2

    print(f"\nYou need {cents // buck} dollar(s), with nominale of: $ {buck // 100} buck")
    cents %= buck

    print(f"\nYou need {cents // cents_25} cent(s), with nominale of: ¢ {cents_25} cents")
    cents %= cents_25

    print(f"\nYou need {cents // cents_10} cent(s), with nominale of: ¢ {cents_10} cents")
    cents %= cents_10

    print(f"\nYou need {cents // cents_5} cent(s), with nominale of: ¢ {cents_5} cents")
    cents %= cents_5

    print(f"\nYou need {cents // cent_1} cent(s), with nominale of: ¢ {cent_1} cent")
    cents %= cent_1

# Exercise ^14
def task14():
    ft = int(input("How much ft` in your height: "))
    inches = int(input("How much inches`` in your height: "))

    foot_in_inch = 12
    inch_in_cm = 2.54

    calc_of = (ft * foot_in_inch + inches) * inch_in_cm
    print(f"Your height in system [SI] will be {round(calc_of)} (cm)")

# Exercise ^15
def task15():
    fts = int(input("Your distance in fts`: "))
    inches = fts * 12
    yd = fts * 0.33333
    mile = fts * 0.00018939

    print(f"\nDistance in miles will be {mile:.2f}. \
    \nDistance in yards will be {yd:.2f}. \
    \nDistance in inches will be {inches}.")

# Exercise ^16
def task16():
    r = int(input("Enter your radius (rad): "))
    area_circle = math.pi * (r ** 2)
    volume_sphere = (4/3) * math.pi * math.pow(r, 3)
    print(f"\nYour area of the circle will be: {area_circle:.2f} (m2). \
    \nYour volume of the sphere will be: {volume_sphere:.2f} (m3).")

# Exercise ^17
def task17():
    water = int(input("Enter the mass of water (grammes): "))
    tinit = float(input("Enter initial temperature (°C): "))
    tend = float(input("Enter temperature at the end (°C): "))

    c_water = 4.18
    absolute_t = tend - tinit
    q = water * c_water * absolute_t

    print(f"\nThe heat (Q) will be: {round(q)} (joules)")

    # ///  convertor from joules to killowatt  ///
    kw = q / 3600000
    price = 8.9 * kw

    print(f"\nPrice for one cup of tea will be: $ {price:.2f}")

# Exercise ^18
def task18():
    r = int(input("Enter radius of cylinder (rad): "))
    h = float(input("Enter height of cylinder (cm): "))
    v = math.pi * math.pow(r, 2) * h
    print(f"\nVolume is: {v:.1f} (cm3)")

# Exercise ^19
def task19():
    h = int(input("Enter please height of object from which you will jump (m): "))
    base_speed = 0
    acceleration = 9.8
    v_free = math.sqrt(math.pow(base_speed, 2) + (2 * acceleration * h))
    print(f"\nFree fall will be: {v_free:.1f} (N)")

# Exercise ^20
def task20():
# /// formule: PV = nRT
# P - pressure (pascales)
# V - volume(liters)
# n - amount of thing (mols) 
# R - const of gas, equal to - 8.314 (joules/(mol*K))
# T - tmp in Kelvins (K) ///
    p = float(input("Enter please pressure (pascales): ").replace(" ", ""))
    v = float(input("Enter please volume (liters): "))
    t = float(input("Enter please temperature (°C): "))

    pv = p * v
    t = t + 273.15
#    convert from celsius to kelvin 
    rt = 8.314 * t
    n = pv / rt

    print(f"\nThe amount of gas (moles) is: {n:.2f}")

# Exercise ^21
def task21():
    b = float(input("Enter a long: "))
    h = float(input("Enter a height: "))
    area = (b * h) / 2
    print(f"\nArea will be: {round(area)} \
    \nLong is: {b} \
    \nHeight is: {h}")

# Exercise ^22
def task22():
    s1 = float(input("Enter long first part of triangle: "))
    s2 = float(input("Enter long second part of triangle: "))
    s3 = float(input("Enter long third part of triangle: "))
    s = sum((s1, s2, s3)) / 2
    area = math.sqrt((s * (s - s1) * (s - s2) * (s - s3)))
    print(f"\nArea will be: {round(area)}")

# Exercise ^23
def task23():
    s = float(input("Enter a long of side: "))
    n = int(input("Enter amount of sides: "))
    area = (n * math.pow(s, 2)) / (4 * (math.tan(math.pi / n)))
    print(f"\nArea is: {round(area)} (m2)")

# Exercise ^24
def task24():
    d = int(input("Enter the amount of days: "))
    hr = int(input("Enter the hours: "))
    m = int(input("Enter the minutes: "))
    s = int(input("Enter the seconds: "))

    sec_ind = d * 24 * 60 * 60
    sec_inhr = hr * 60 * 60
    sec_inm = m * 60
    summary = sum((sec_ind, sec_inhr, sec_inm, s))
    print(f"\nTotal amount of seconds is: {summary}")

# Exercise ^25
def task25():
    d = int(input("Enter the amount of days: "))
    hr = int(input("Enter the hours: "))
    m = int(input("Enter the minutes: "))
    s = int(input("Enter the seconds: "))

    sec_ind = d * 24 * 60 * 60
    sec_inhr = hr * 60 * 60
    sec_inm = m * 60
    summary = sum((sec_ind, sec_inhr, sec_inm, s))
    print(f"\nTotal amount of seconds is: {summary}")
    # ///
    d_sring = str(d)
    hr_string ="%2s" % str(hr)
    m_string = "%2s" % str(m)
    sec_string = "%2s" % str(s)
    print(f"{d_sring}:{hr_string}:{m_string}:{sec_string}".replace(" ", "0"))
    
# Exercise ^26
def task26():
    a = time.asctime()
    print(f"\nCurrent time is: {a}")

# Exercise ^27
def task27():
    year = int(input("Enter the year: "))
    a = year % 19
    b = math.floor(year / 100)
    c = year % 100
    d = math.floor(b / 4)
    e = b % 4
    f = math.floor((b + 8) / 25)
    g = math.floor((b - f + 1) / 3)
    h = (19 * a + b - d - g + 15) % 30
    i = math.floor(c / 4)
    k = c % 4
    l = (32 + (2 * e) + (2 * i) - h - k) % 7
    m = math.floor((a + 11 * h + 22 * l) / 451)
    month = (h + l + (7 * m) + 114) / 31
    day = ((h + l - 7 * m + 114) % 31) + 1

    print(f"The month will be: {int(month)}\nThe day will be: {day}")

# Exercise ^28
def task28():
# if users inputs are in inches, fts, pounds
    # bmi_notinCI = (weight / math.pow(height, 2)) * 703
    # print(f"Your body mass index is: {bmi_notinCI}")
    height = float(input("Enter your height: ")),
    weight = float(input("Enter your weight: "))
 
    bmi = weight / math.pow(height, 2)
    print(f"Your body mass index is: {bmi:.4f}")

# Exercise ^29
def task29():
    ta = float(input("Enter temperature of winds (°С): "))
    v = float(input("Enter the speed of winds: "))
    wci = 13.12 + 0.6215 * ta - 11.37 * (v ** 0.16) + 0.3965 * (ta * (v ** 0.16))
    print(f"Cofficient is: {math.ceil(wci)}")
    # WCI = 13.12 + 0.6215 * Ta - 11.37 * V0.16 + 0.3965 * Tav0.16

# Exercise ^30
def task30():
    cels = float(input("Enter a tempreture in Celsius: "))
    kelvin = cels + 273.15
    fahr = (cels * 9/5) + 32
    print(f"\nIn Fahrenheit: {fahr:.2f}\nIn Kelvin: {kelvin:.2f}")

# Exercise ^31
def task31():
    press = float(input("Enter please value of pressure: "))
    psi = press / 6.895
    mercury = press * 7.501
    atmo = press / 101.3 
    print(f"\nYour output will be: \
    \n{psi:.2f} in PSI, \
    \n{mercury:.2f} in mm of mercury, \
    \n{atmo:.2f} in atmosphere")

# Exercise ^32
def task32():
    n = input("Enter your number: ")
    listed = list(map(int, n))
    summary = sum(listed)
    print(summary)

# Exercise ^33
def task33():
    n1 = int(input("Enter a first number: "))
    n2 = int(input("Enter a second number: "))
    n3 = int(input("Enter a third number: "))

    listed = [n1, n2, n3]
    s = sorted(listed)
    print(f"{s[0]}, {s[1]}, {s[2]}")
#  /// another solution
    mn = min(listed)
    mx = max(listed)
    sum_minused = sum(listed) - mn - mx
    print(f"{mn}, {sum_minused}, {mx}")

# Exercise ^34
def task34():
    a = int(input("Enter amount of breads: "))
    base_price = 3.49 * a
    # discount is 60%
    discounted = base_price * 0.6
    total = base_price - discounted
    print(f"\nBase price of bread is: $ {base_price:.2f} \
          \nDiscount amount: $ {discounted:.2f} \
          \nYour total price for your breads: $ {(total):.2f}")

# Chapter ^2
# Exercise ^35
def task35():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"Your num {num} is even.")
    else:
        print(f"Your num {num} is odd.")

# Exercise ^36
def task36():
    human_year = int(input("Enter amount of years: "))
    dog_year = 0
    if human_year <= 2:
        dog_year = human_year * 10.5
        print(f"Year for dog will be: {dog_year}")
    elif human_year >= 2:
        dog_year += 21
        dog_year = dog_year + (human_year - 2) * 4
        print(f"Year for dog will be: {dog_year}")
    else:
        print(f"Incorrect value of input...///")

def task37():
    letter = input("Enter a letter: ")
    vowels = ["a", "e", "i", "o", "u"
              "A", "E", "I", "O", "U"]
    if letter in vowels:
        print(f"Yes, correct your letter |{letter}| is vowel.")
    elif letter == "y":
        print("Y/y is vowel and at the same time is not.")
    else:
        print(f"Unfortunately, your letter |{letter}| is consonant.")

def task38():
    dict_figs = {
        "3": "triangle", "4": "square", 
        "5": "pentagon", "6": "hexagon",
        "7": "heptagon", "8": "octagon",
        "9": "nonagon", "10": "decagon"
    }
    angle_inp = input("Enter a value of angles (3-10): ")
    if angle_inp in dict_figs:
        print(f"Your figure is: {dict_figs[angle_inp]}")
    else:
        print(f"Your input is out of the range 3-10")

def task39():
    monthToDay = {1: 31, 2: 28, 3: 31, 4: 30,
                 5: 31, 6: 30, 7: 31, 8: 31, 
                 9: 30, 10: 31, 11: 30, 12: 31}
    
    m_inp = int(input("Enter a number of month (1-12): "))

    if m_inp in monthToDay:
        print(f"In this month will be: {monthToDay[m_inp]}")
    else:
        print("Incorrect input")

def task40():

    dict_items = {
        130: "Jackhammer",
        106: "Gas lawn mower",
        70: "Alarm clock",
        40: "Quiet room"
    }

    db_inp = int(input("Enter a level of noise in range [40 - 130] (db): "))

    if db_inp in dict_items:
        print(f"Value {db_inp} for {dict_items[db_inp]}")

    elif 70 > db_inp > 40:
        print(f"Value {db_inp} between {dict_items[70]} and {dict_items[40]}")
    elif 106 > db_inp > 70:
        print(f"Value {db_inp} between {dict_items[106]} and {dict_items[70]}")
    elif 130 > db_inp > 106:
        print(f"Value {db_inp} between {dict_items[130]} and {dict_items[106]}")
    else:
        print(f"Value is not in range [40 - 130]")

def task41():
    first_angle = float(input("Enter a value of first angle: "))
    second_angle = float(input("Enter a value of second angle: "))
    third_angle = float(input("Enter a value of first angle: "))

    list_angles = list((first_angle, second_angle, third_angle))

    mn = min(list_angles)
    mx = max(list_angles)
    
    # summary = sum(list_angles)
    # if (summary / 3) == first_angle:
    #     print("Your triangle is Equilateral")
    if mn == mx:
        print("Your triangle is Equilateral")

    elif list_angles[0] == list_angles[1] \
    or list_angles[0] == list_angles[2] \
    or list_angles[1] == list_angles[2]:

        print(f"Your triangle is Isosceles")
    else:
        print(f"Your triangle is Scalene")


def task42():
    notes = {"C": 261.63,  "D": 293.66,
              "E": 329.63, "F": 349.23, 
              "G": 392.00, "A": 440.00, "B": 493.88}
    # all notes in 4-th octave
    
    note = input("Enter a value of note (C - B) in range of [0-8]: ")
    
    note_octave = list(note)
    if note_octave[0] in notes:
        octave = int(note_octave[1])
        if 0 <= octave <= 8:
            calc = notes[note_octave[0]] / 2 ** (4 - octave)
            print(calc)
        else:
            print("Invalid input")

def task43():
    hz = float(input("Enter a value of sound (Hz): "))
    c = 261.63
    d = 293.66
    e = 329.63
    f = 349.23
    g = 392.00
    a = 440.00
    b = 493.88
    name_notes = {c:"C", d:"D", e:"E", f:"F", g:"G", a:"A", b:"B"}

    if any(val - 1 <= hz <= val + 1 for val in name_notes):
        for val in name_notes:
            if val - 1 <= hz <= val + 1:
                print(f"This note is {name_notes[val]}")
    else:
        print("NOT FOUND")


def task44():
    banknotes = {
        1: "George Washington",
        2: "Tomas Jefferson",
        5: "Abraham Lincoln", 
        10: "Alexander Hammilton",
        20: "Andrew Jackson",
        50: "Willis Grant",
        100: "Benjamin Franklin"
    }
    value_banknote = int(input("Enter a value of your banknote: $ "))

    if value_banknote in banknotes:
        print(f"On your banknote depicted {banknotes[value_banknote]}")
    else:
        print("Your value is incorrect, nominale of banknotes is: 1, 2, 5, 10, 20, 50 and 100 dollars.")

def task45():
    holidays = {
        "1 January": "New Year",
        "1 July": "Canada Day",
        "25 December": "Christmas"
    }
    val_user = input("Enter day and month: ")
    if val_user in holidays:
        print(f"Your holiday is: {holidays[val_user]}.")
    else:
        print("Your date is not a holiday.")

def task46():
    coordinates_black = {
        "a1", "a3", "a5", "a7", 
        "b2", "b4", "b6", "b8",
        "c1", "c3", "c5", "c7",
        "d2", "d4", "d6", "d8",
        "e1", "e3", "e5", "e7",
        "f2", "f4", "f6", "f8",
        "g1", "g3", "g5", "g7",
        "h2", "h4", "h6", "h8"
    }
    # method_black = {coord: "black" for coord in coordinates_black}
    coordinate = input("Enter a coordinate of square (for example - a1): ")

    if coordinate in coordinates_black:
        print(f"Your square {coordinate} is: black")
    else:
        print(f"Your square {coordinate} is: white")

def task47():
    months = {
        "Март 20" : "Весна",
        "Июнь 21" : "Лето",
        "Сентябрь 22" : "Осень",
        "21 Декабря" : "Зима"
    }

    inp = input("Enter a day and month: ")
    
    if inp in months:
        print(f"{months[inp]}")

def task48():

    zodiacs = ["Козерог", "Водолей", "Рыбы",
                "Овен", "Телец", "Близнецы",
                "Рак", "Лев", "Дева",
                "Весы", "Скорпион", "Стрелец"]
    
    months = {
        "Января": 1, "Февраля": 2,
        "Марта": 3, "Апреля": 4,
        "Мая": 5, "Июня": 6,
        "Июля": 7, "Августа": 8,
        "Сентября": 9, "Октября": 10,
        "Ноября": 11, "Декабря": 12,
    }

    user_birth = input("Введите дату вашего рождение (число и месяц): ")

    date = user_birth.split()
    number = int(date[0])
    month = date[1].capitalize()

    if month in months:
        if (number in range(22, 31 + 1) or number in range(1, 19 + 1)) and months[month] == 1:
            print(zodiacs[0])
        elif number in range(20, 31 + 1) or number in range(1, 18 + 1) and months[month] == 2:
            print(zodiacs[1])
        elif number in range(19, 28 + 1) or number in range(1, 20 + 1) and months[month] == 3:
            print(zodiacs[2])
        elif number in range(21, 31 + 1) or number in range(1, 19 + 1) and months[month] == 4:
            print(zodiacs[3])
        elif number in range(20, 30 + 1) or number in range(1, 20 + 1) and months[month] == 5:
            print(zodiacs[4])
        elif number in range(21, 31 + 1) or number in range(1, 20 + 1) and months[month] == 6:
            print(zodiacs[5])
        elif number in range(21, 30 + 1) or number in range(1, 22 + 1) and months[month] == 7:
            print(zodiacs[6])
        elif number in range(23, 31 + 1) or number in range(1, 22 + 1) and months[month] == 8:
            print(zodiacs[7])
        elif number in range(23, 31 + 1) or number in range(1, 22 + 1) and months[month] == 9:
            print(zodiacs[8])
        elif number in range(23, 30 + 1) or number in range(1, 22 + 1) and months[month] == 10:
            print(zodiacs[9])
        elif number in range(23, 31 + 1) or number in range(1, 21 + 1) and months[month] == 11:
            print(zodiacs[10])
        elif number in range(22, 30 + 1) or number in range(1, 21 + 1) and months[month] == 12:
            print(zodiacs[11])
    else:
        pass

def task49():
    animals = {2000: "Дракон", 2001: "Змея", 2002: "Лошадь",
               2003: "Коза", 2004: "Обезьяна", 2005: "Петух",
               2006: "Собака", 2007: "Свинья", 2008: "Крыса",
               2009: "Бык", 2010: "Тигр", 2011: "Кролик"
}
    user_birth = int(input("Enter your year of birth: "))
    if user_birth in animals:
        print(animals[user_birth])


def task50():
    user_magnitude = float(input("Enter a value of magnitude: "))
    description = (
        "Минимальное" if user_magnitude < 2.0 else
        "Очень слабое" if user_magnitude < 3.0 else
        "Слабое" if user_magnitude < 4.0 else
        "Промежуточное" if user_magnitude < 5.0 else
        "Умеренное" if user_magnitude < 6.0 else
        "Сильное" if user_magnitude < 7.0 else
        "Очень сильное" if user_magnitude < 8.0 else
        "Огромное" if user_magnitude < 10.0 else
        "Разрушительное"
    )
    print(f"Описание землетрясения: {description}")


def task51():
    import math
    users_a_val = int(input("Enter a value of [a]: "))
    users_b_val = int(input("Enter a value of [b]: "))
    users_c_val = int(input("Enter a value of [c]: "))

    discriminant = users_b_val ** 2 - 4 *users_a_val * users_c_val

    if discriminant < 0:
        print("\nD is negative, that's why sollutions are impossible to calculate...\n")
        return

    discriminant_sqrt = math.sqrt(discriminant)

    x1 = (-(users_b_val) + discriminant_sqrt) / (2 * users_a_val)
    x2 = (-(users_b_val) - discriminant_sqrt) / (2 * users_a_val)

    solution_one = users_a_val*(x1**2) + users_b_val*x1 + users_c_val
    solution_two = users_a_val*(x2**2) + users_b_val*x2 + users_c_val

    if solution_one == 0 and solution_two == 0:
        print(f"\nAll solutions [{x1, x2}] are correct\n")
        print(f"Solution one was: {solution_one}")
        print(f"Solution two was: {solution_two}")
    elif solution_one == 0:
        print(f"\nOnly solution one [{x1}] is correct\n")
        print(f"Solution one was: {solution_one}")
    elif solution_two == 0:
        print(f"\nOnly solution two [{x2}] is correct")
        print(f"Solution two was: {solution_two}")
    else:
        print(f"\nNone of the solutions [{x1, x2}] aren't correct")

def task52():
    # Упражнение 52. Буквенные оценки – в числовые
    user_mark = input("Enter a value of mark (from A+ to F): ")
    marks = (
        4.0 if user_mark == "A+" or user_mark == "A" else
        3.7 if user_mark == "A-" else
        3.3 if user_mark == "B+" else
        3.0 if user_mark == "B" else
        2.7 if user_mark == "B-" else
        2.3 if user_mark == "C+" else
        2.0 if user_mark == "C" else
        1.7 if user_mark == "C-" else
        1.3 if user_mark == "D+" else
        1.0 if user_mark == "D" else
        0 if user_mark == "F" else
        "Incorrect value of mark"
    )
    print(f"Your mark in nums wiil be: {marks}")

def task53():
    # Упражнение 53. Числовые оценки – в буквенные
    user_mark = float(input("Enter a value of mark (from 0 to 4.0+): "))

    if user_mark >= 4.0:
        mark = "A+"
    elif user_mark >= 3.7:
        mark = "A"
    elif user_mark >= 3.3:
        mark = "A-"
    elif user_mark >= 3.0:
        mark = "B+"
    elif user_mark >= 2.7:
        mark = "B"
    elif user_mark >= 2.3:
        mark = "B-"
    elif user_mark >= 2.0:
        mark = "C+"
    elif user_mark >= 1.7:
        mark = "C"
    elif user_mark >= 1.3:
        mark = "C-"
    elif user_mark >= 1.0:
        mark = "D+"
    elif user_mark >= 1.0:
        mark = "D"
    elif user_mark == 0:
        mark = "F"
    else:
        mark = "Incorrect value of mark"
    
    print(f"Your mark in letters will be: {mark}")


def main():
    while True:
        choice = input("\nEnter a number of task (at the moment range is in [1 - 53])\
        \nor enter [stop] if you wanna stop program : ")
        tasks = {
    '1': task1, '2': task2, '3': task3, '4': task4, '5': task5,
    '6': task6, '7': task7, '8': task8, '9': task9, '10': task10,
    '11': task11, '12': task12, '13': task13, '14': task14, '15': task15,
    '16': task16, '17': task17, '18': task18, '19': task19, '20': task20,
    '21': task21, '22': task22, '23': task23, '24': task24, '25': task25,
    '26': task26, '27': task27, '28': task28, '29': task29, '30': task30,
    '31': task31, '32': task32, '33': task33, '34': task34, '35': task35,
    '36': task36, '37': task37, '38': task38, '39': task39, '40': task40,
    '41': task41, '42': task42, '43': task43, '44': task44, '45': task45,
    '46': task46, '47': task47, '48': task48, '49': task49, '50': task50,
    '51': task51, '52': task52, '53': task53,

}
        if choice == "stop":
            print("Program was stopped///...\n")
            break
        elif choice in tasks:
            print("\n")
            tasks[choice]()
        else:
            print(f"Your input |{choice}| isn't correct, please enter a number in range [1 - 34]\n")
if __name__ == "__main__":
    main()