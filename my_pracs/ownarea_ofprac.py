def nameNmail():
    print("Oleksii Khodus")
    print("exalchel@gmail.com")
nameNmail()


def greeting(name):
    print(f"Nice to meet you {name}")
greeting(input("Enter your name please: "))


def calc_area(leng, wid):
    calc = leng * wid
    print(f"Your area is {int(calc)} (m^2)")

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

    print(f"\nTax (20%) for this order is: ${tax:.2f}\nTips (18%) for this order is: ${tips:.2f}\nSummary of all of this: ${summary:.2f}")

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

import math 

def arith(a, b):
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

arith(int(input("Enter your first number: ")), int(input("Enter your second number: ")))

def converter_fuel(fuel):
    L100km = (282.48 / fuel)
    print(f"In Canada you'll have {L100km:.2f} L/100 km.") 

converter_fuel(float(input("Enter how much MPG (miles-per-gallon) fuel your car uses: ")))

import math

def distance_btw():
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

distance_btw()

def change(cents):
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

change(int(input("Enter a value of cents: ¢ ")))


def height(ft, inches):
    foot_in_inch = 12
    inch_in_cm = 2.54

    calc_of = (ft * foot_in_inch + inches) * inch_in_cm
    print(f"Your height in system [SI] will be {round(calc_of)} (cm)")

height(int(input("How much ft` in your height: ")),int(input("How much inches`` in your height: ")))


def distance_in_america(fts):
    inches = fts * 12
    yd = fts * 0.33333
    mile = fts * 0.00018939

    print(f"\nDistance in miles will be {mile:.2f}.\nDistance in yards will be {yd:.2f}.\nDistance in inches will be {inches}.")

distance_in_america(int(input("Your distance in fts`: ")))

import math

def radius(r):
    area_circle = math.pi * (r ** 2)
    volume_sphere = (4/3) * math.pi * math.pow(r, 3)
    print(f"\nYour area of the circle will be: {area_circle:.2f} (m2).\nYour volume of the sphere will be: {volume_sphere:.2f} (m3).")

radius(int(input("Enter your radius (rad): ")))


def heat_capacity(water, tinit, tend):
    c_water = 4.18
    absolute_t = tend - tinit
    q = water * c_water * absolute_t

    print(f"\nThe heat (Q) will be: {round(q)} (joules)")

    # ///  convertor from joules to killowatt  ///
    kw = q / 3600000
    price = 8.9 * kw

    print(f"\nPrice for one cup of tea will be: $ {price:.2f}")

heat_capacity(
    int(input("Enter the mass of water (grammes): ")), 
    float(input("Enter initial temperature (°C): ")), 
    float(input("Enter temperature at the end (°C): "))
)

import math

def volume_cylinder(r, h):
    v = math.pi * math.pow(r, 2) * h
    print(f"\nVolume is: {v:.1f} (cm3)")

volume_cylinder(
    int(input("Enter radius of cylinder (rad): ")),
    float(input("Enter height of cylinder (cm): "))
)

import math

def free_fall(h):
    base_speed = 0
    acceleration = 9.8
    v_free = math.sqrt(math.pow(base_speed, 2) + (2 * acceleration * h))
    print(f"\nFree fall will be: {v_free:.1f} (N)")

free_fall(int(input("Enter please height of object from which you will jump (m): ")))


def ideal_gas(p, v, t):
# /// formule: PV = nRT
# P - pressure (pascales)
# V - volume(liters)
# n - amount of thing (mols) 
# R - const of gas, equal to - 8.314 (joules/(mol*K))
# T - tmp in Kelvins (K) ///

   pv = p * v
   t = t + 273.15
#    convert from celsius to kelvin 
   rt = 8.314 * t
   n = pv / rt

   print(f"\nThe amount of gas (moles) is: {n:.2f}")

ideal_gas(
    float(input("Enter please pressure (pascales): ").replace(" ", "")),
    float(input("Enter please volume (liters): ")),
    float(input("Enter please temperature (°C): "))
)

def area_triangle(b, h):
    area = (b * h) / 2
    print(f"\nArea will be: {round(area)}\nLong is: {b}\nHeight is: {h}")

area_triangle(float(input("Enter a long: ")), float(input("Enter a height: ")))


import math

def area_triangle2(s1, s2, s3):
    s = sum((s1, s2, s3)) / 2
    area = math.sqrt((s * (s - s1) * (s - s2) * (s - s3)))
    print(f"\nArea will be: {round(area)}")

area_triangle2(
    float(input("Enter long first part of triangle: ")),
    float(input("Enter long second part of triangle: ")),
    float(input("Enter long third part of triangle: "))
)

import math

def correct_angles(s, n):
    area = (n * math.pow(s, 2)) / (4 * (math.tan(math.pi / n)))
    print(f"\nArea is: {round(area)} (m2)")

correct_angles(
    float(input("Enter a long of side: ")),
    int(input("Enter amount of sides: "))
)

def time(d, hr, m, s):
    sec_ind = d * 24 * 60 * 60
    sec_inhr = hr * 60 * 60
    sec_inm = m * 60
    summary = sum((sec_ind, sec_inhr, sec_inm, s))
    print(f"\nTotal amount of seconds is: {summary}")

time(
    int(input("Enter the amount of days: ")),
    int(input("Enter the hours: ")),
    int(input("Enter the minutes: ")),
    int(input("Enter the seconds: "))
)

def time_updated(d, hr, m, s):
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
    
time_updated(
    int(input("Enter the amount of days: ")),
    int(input("Enter the hours: ")),
    int(input("Enter the minutes: ")),
    int(input("Enter the seconds: "))
)


import time

def current_time():
    a = time.asctime()
    print(f"\nCurrent time is: {a}")
current_time()

import math

def when_easter(year):
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

when_easter(int(input("Enter the year: ")))

import math

def body_mass_index(height, weight):
# if users inputs are in inches, fts, pounds
    # bmi_notinCI = (weight / math.pow(height, 2)) * 703
    # print(f"Your body mass index is: {bmi_notinCI}")
 
    bmi = weight / math.pow(height, 2)
    print(f"Your body mass index is: {bmi:.4f}")

body_mass_index(
    float(input("Enter your height: ")),
    float(input("Enter your weight: "))
)

import math

def temp_wind(ta, v):
    wci = 13.12 + 0.6215 * ta - 11.37 * (v ** 0.16) + 0.3965 * (ta * (v ** 0.16))
    print(f"Cofficient is: {math.ceil(wci)}")
    # WCI = 13.12 + 0.6215 * Ta - 11.37 * V0.16 + 0.3965 * Tav0.16
temp_wind(
    float(input("Enter temperature of winds (°С): ")),
    float(input("Enter the speed of winds: "))
)