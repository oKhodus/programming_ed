def done():
        # Ex1
    def greet(name):
        str_name = f"Hello, {name}"
        print(str_name)
        return str_name


    greeting = greet("Alexey")
    print(greeting)


    # Ex2
    def check_password(password):
        correct_password = "mypassword123"
        pass_name = f'{password} is {{}}'
        if password == correct_password:
            print(pass_name.format("True"))
            return True
        else:
            print(pass_name.format("False"))
            return False


    is_valid = check_password("mypassword123")
    print(is_valid)


    # Ex3
    def add_numbers(a, b):
        summary = a + b
        print(summary)
        return summary


    result = add_numbers(5, 3)
    print(result)


    # Ex4
    def notify_purchase(purchases):
        purchases_string = f"You have bought {', '.join(purchases)}"
        print(purchases_string)
        return purchases_string


    num_purchases = notify_purchase(["apples", "bread", "milk"])
    print(num_purchases)


    # Ex5
    #  F = C * 9/5 + 32

    def convert_temp(celsius):
        fahr = celsius * 9 / 5 + 32
        print(f"In Fahrenheit it will be {fahr}")
        return fahr


    converted = convert_temp(float(input("Enter in celsius: ")))
    print(converted)



    def done_program():
        largest = None
        smallest = None
        while True:
            num = input("Enter a number: ")
            if num == "done":
                break
            try:
                num_int = int(num)
            except ValueError:
                print("Invalid input")
                continue
            if largest is None or num_int > largest:
                largest = num_int
            elif smallest is None or num_int < smallest:
                smallest = num_int
        if largest is not None and smallest is not None:
            print("Maximum is", largest)
            print("Minimum is", smallest)
        else:
            print("No numbers entered")

    done_program()

    def amount_of_nums(n):
        for i in range(1, n):
            n += i
        print(n)
    amount_of_nums(int(input("Enter a number: ")))

    def even_nums(n):
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i)
    even_nums(int(input("Enter a number: ")))

    def factorial(n):
        for i in range(1, n):
            n *= i
        print(n)
    factorial(int(input("Enter a number: ")))

    def reverse_line(n):
        for i in range(n, 0, -1):
            n -= i
            print(i)
    reverse_line(int(input("Enter a number: ")))

    def sum_even_nums(n):
        total = 0
        for i in range(1,n+1):
            if i % 2 == 0:
                total = i + i
        print(total)
    sum_even_nums(int(input("Enter a number: ")))



    def sqr_nums(n):
        total = 0
        for i in range(1,n+1):
            total = i ** 2
            print(total)

    sqr_nums(int(input("Enter a number: ")))

    def sum_str(n):
        total = 0
        for symbol in n:
            sym_int = int(symbol)
            total = total + sym_int
        print(total)

    sum_str(input("Enter a number: "))


    def tabl(n):
        for i in range(1, 11):
            print(f"{n} * {i} = {n * i}")

    tabl(int(input("Enter a number: ")))

    # def fibonacci(n):
    # fibonacci(int(input("Enter a number: ")))

    def reverse_str(n):
        rev ="".join(reversed(n))
        print(rev)

    reverse_str(input("Enter a number: "))
    a,b,c,d = map(int, input().split())
    if b > a:
        a, b = b, a
    if d > c:
        c, d = d, c 
    print("ДА" if a - c >= 2 and b - d >= 2 else "НЕТ")

    inp = list(map(str, input()))
    part1 = list(map(int, inp[:3]))
    part2 = list(map(int, inp[3:]))
    out1 = 0
    out2 = 0
    for elem in part1:
        out1 += elem
    for elem2 in part2:
        out2 += elem2
    print("ДА" if out1 == out2 else "НЕТ")

    inp = float(input())
    print("green" if round(inp) % 3 == 0 else "red")

    m = '''1. Введение в Python
    2. Строки и списки
    3. Условные операторы
    4. Циклы
    5. Словари, кортежи и множества
    6. Выход'''

    user_num = input()
    lines = m.splitlines()

    if user_num in lines[0]:
        main_str = lines[0]
    elif user_num in lines[1]:
        main_str = lines[1]
    elif user_num in lines[2]:
        main_str = lines[2]
    elif user_num in lines[3]:
        main_str = lines[3]
    elif user_num in lines[4]:
        main_str = lines[4]
    else:
        main_str = lines[5]

    print(main_str)
# ////////
    a, b, c = map(int, input().split())

    if a <= b and a <= c:
        less = a
    elif b <= a and b <= c:
        less = b
    else:
        less = c

    print(less)
# ////////
    day = int(input())

    days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

    out = days[day-1] if days[day-1] in days else "Incorrecto"

    print(out)
# ////////
    month = int(input())
    months = range(1, 13)

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    print(days_in_month[month-1]) if month in months else print("Incorrecto")


    month, day = map(int, input().split())
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def ytd(month, day):
        if day > 1:
            yesterday = f"{month:02}.{day-1:02}"
        else:
            if month == 1:
                yesterday = f"12.{days_in_month[month+10]:02}"
            else:
                previous_month = month - 1
                yesterday = f"{previous_month:02}.{days_in_month[previous_month-1]:02}"
        return yesterday

    def trw(month, day):
        if day < days_in_month[month-1]:
            tomorrow = f"{month:02}.{day+1:02}"
        else:
            if month == 12:
                tomorrow = f"01.01"
            else:
                next_month = month + 1
                tomorrow = f"{next_month:02}.01"
        return tomorrow

    print(ytd(month, day), trw(month, day))
# ////////
    k = int(input())
    days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    if 1 <= k <= 365:
        a = k % 7
        print(days[a-1])
    else:
        print('incorrect')
# ////////
    a = input().lower()
    print("палиндром" if a == a[::-1] else "не палиндром")
# ////////
    sec = range(0, 60)
    user_sec = int(input())
    user_sec = (0 if user_sec == 59 else user_sec + 1) if user_sec > -1 else None
    print(user_sec)
# ////////
    m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
    a, b, c = map(int, input().split())

    out = []

    out.append("#" + m[a-1]) if m[a-1] == "до" or m[a-1] == "фа" else out.append(m[a-1])
    out.append("#" + m[b-1]) if m[b-1] == "до" or m[b-1] == "фа" else out.append(m[b-1])
    out.append("#" + m[c-1]) if m[c-1] == "до" or m[c-1] == "фа" else out.append(m[c-1])

    print(*out)
# ////////
    x = float(input())
    out = []
    summ = 0
    for elem in range(2, 11):
        summ = elem * x
        out.append(f"{summ:.1f}")
    print(*out)
# ////////
    n = int(input())
    summ = 1
    s = 1
    while summ < n:
        summ += 1
        s += 1/summ
    print(f"{s:.3f}")
# ////////
    n = int(input())
    summ = 0
    while n != 0:
        summ += n
        n = int(input())
    print(summ)
# ////////
    inp = input().split("-")
    out = ''
    for elem in inp:
        if elem != '' and elem != inp[-1]:
            out += elem
            out += "-"
        else:
            out += elem
    print(out)
# ////////
    n = int(input())
    summ = 1
    for elem in str(n):
        summ *= int(elem)
    print(summ)

# ////////
    n = int(input())
    first = 1
    second = 1
    print(first, second, end=' ')
# ////////
    for step in range(0, n-2):
        summ = first + second
        first = second
        second = summ
        step+=1
        print(second, end=' ')

    amoeba = 1
    n = int(input())
    while n > 0:
        n -= 3
        amoeba *= 2
        if n < 3:
            break
    print(amoeba)
# ////////
    a, b = (int, input().split())
    for elem in range(2, 10):
        if elem % 2 != 0:
            print(elem, end=" ")

    for elem in range(100, 1000):
        if elem % 47 == 43 and elem % 3 == 0:
            print(elem, end=" ")
# ////////
    p = [0] * 10

    lst = []
    cop = p.copy()
    i = -1
    while i <= 5:
        i += 1
        n = int(input())
        if p[n] != 1:
            p[n] = 1
        else:
            continue
    print(*p)

# ////////
    step = 1
    while (n := int(input())) != 0:
        if n > 0:
            step *= n      
        else:
            continue
    print(step)
# ////////
    lst = list(map(str, input().split()))
    output = []
    for elem in lst:
        if len(elem) > 5:
            output.append(1)
        else:
            output.append(0)
    print("ДА" if all(output) == 1 else "НЕТ")
# ////////
    a = list(map(str, input().split()))
    out = []
    for name in a:
        if name[0].lower() == name[-1:].lower():
            out.append("ДА")
        else:
            out.append("НЕТ")

    print("ДА" if "ДА" in out else "НЕТ")
# ////////
    n = int(input())
    out = []

    if n < 100:
        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                out.append(num)
        print(*out)
    else:
        print("слишком большое значение n")
# ////////
    n = int(input())
    for num in range(1, n+2):
        if (num ** 2) > n:
            print(num)
            break
# ////////
    x = int(input())
    day = 1
    distance = 10
    while distance <= x:
        
        distance += (distance * 0.1)
        day += 1
        print(distance)
    print(day)
# ////////
    import sys 
    lst_in = list(map(str.strip, sys.stdin.readlines()))
    res = []
    for elem in lst_in:
        if " " not in elem:
            res.append(elem)
    print(*res, end=" ")
# ////////
    for n in range(1, 20, 3):
        print(n, end=" ")
    
    lst = list(map(int, input().split()))
    summ = 0
    for n in lst:
        if n % 2 != 0:
            summ += n
    print(summ)
# ////////
    inp = list(map(str, input().split()))
    for word in inp:
        print(len(word), end=" ")
# ////////
    n = int(input())
    for num in range(1, n+1):
        if n % num == 0:
            print(num)
# ////////
    n = int(input())
    lst = []
    for num in range(1, n+1):

        out = "ДА" if n % num == 0 else "НЕТ"
        lst.append(out)
        
    print("ДА" if lst.count("ДА") == 2 else "НЕТ")
# ////////
# алгоритм, который проверяет правила игры в города
    lst = list(map(str, input().split()))
    inc = ['ь', 'ъ', 'ы']
    ends = []
    out = []
    for city in lst:
        if city[-1:] in inc:
            ends.append(city[-2:-1].upper())
        else:
            ends.append(city[-1:].upper())
        if city[0] in ends:
            out.append("ДА")
        else:
            out.append("НЕТ")

    print("ДА" if out.count("ДА") >= len(lst) - 1 else "НЕТ")
# ////////
    n = int(input())
    out = []
    for integer in range(1, n):
        if integer % 3 == 0 or integer % 5 == 0:
            out.append(integer)
    print(sum(out))
# ////////
    inp = str(input())
    out = []
    for index, char in enumerate(inp):
        if char == "р" and index + 1 < len(inp) and\
        inp[index + 1] == "а":
            out.append(index)
        else:
            continue

    print(-1) if out == [] else print(*out)
# ////////
    inp = list(map(int, input().split()))

    for index, integer in enumerate(inp):
        if index % 2 == 0:
            print(integer, end=" ")
# ////////
    inp = str(input())
    for index, char in enumerate(inp):
        if char == 'а':
            print(index, end=" ")
# ////////
    inp = list(map(int, input().split()))
    out = []
    for index, integer in enumerate(inp):
        if index % 2 != 0:
            out.append(integer)
            out.append(integer - 1)
    print(*out)
# ////////
    inp = list(map(str, input().split()))
    out = []
    for index, word in enumerate(inp):
        out.append(len(word))
    print(f"index: {index}, len: {max(out)}, word: {word}")
# ////////
    inp = list(map(int, input().split()))
    out = []
    for index, integer in enumerate(inp):
        out.append(integer * index)
    print(*out)
# ////////
    inp = list(map(str, input().split()))
    out = []
    for index, elem in enumerate(inp):
        if index % 3 == 0:
            out.append(elem)
    print(*out)
# ////////
    inp = str(input().split())
    base = []
    for elem in inp:
        if elem.isnumeric():
            base.append("x")
    if len(base) == 11 and "+" in inp and len(inp) == 20 and inp[3] == "7":
        print("ДА")
    else:
        print("НЕТ")
# ////////


        def main():
            expr = input().replace("+", " ").split(" ")
            minused_lst = []
            plussed = []
            for index, elem in enumerate(expr):
                if elem == "-":
                    minused = expr[index+1].replace(expr[index+1], "-" + expr[index+1])
                    minused_lst.append(int(minused))
                    expr.remove(expr[index+1])
                elif elem.isdigit():
                    plussed.append(int(elem))
                elif len(elem) > 2:
                    if "-" in elem:
                        minused_exp = elem.split("-")
                        minused_lst.append(int("-" + minused_exp[1]))
                        plussed.append(int(minused_exp[0]))
                    else:
                        plussed_exp = elem.split("+")
                        plussed.append(int(plussed_exp[0]))
                        plussed.append(int(plussed_exp[1]))
                else:
                    continue
            print(sum(plussed + minused_lst))
        
        
        def main2():
            lst = list(map(int, input().split()))
            for index, integer in enumerate(lst):
                print((integer ** 2), end = " ")
        
        def main3():
            lst = list(map(int, input().split()))
            for index, integer in enumerate(lst):
                print(integer, integer, end=" ")
        
        def main4():
            lst = list(map(float, input().split()))
            a = lst[0]
            for index, f in enumerate(lst):
                if f < a:
                    a = f
                else:
                    continue
            print(a)
        
        def main5():
            lst = list(map(float, input().split()))
            for i, n in enumerate(lst):
                if n < 0:
                    n = -1.0
                print(n, end=" ")
        
        
        def main6():
            stdin = input().split(" ")
            city = iter(stdin)
            print(next(city))
            print(next(city))
        
        def main7():
            stdin = iter(input())
            for elem in stdin:
                if elem == " ":
                    break
                else:
                    print(elem, end="")
        
        def main8():
            n = int(input())
            for i in range(1, n+1):
                for j in range(1, n+1):
                    print(1, end=" ") if j != n else print(5)
                