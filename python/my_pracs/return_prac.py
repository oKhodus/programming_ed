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
    
        
    import sys                
    def main():
        
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        app = []
        
        for elem in lst_in:
            st = ""
            for index, sym in enumerate(elem):
                if sym == " ":
                    if elem[index+1] != " ":
                        sym = "-"
                        st += sym
                    else:
                        sym = ""
                        st += sym
                else:
                    st += sym
            app.append(st)

        for line in app:
            print(line, end="\n")

    def main():
        n = int(input())

        for Int in range(2, n):
            prime = True
            for sub_Int in range(2, Int):
                if Int % sub_Int == 0:
                    prime = False
            if prime == True:
                print(Int, end=" ")
                
    import sys

    # считывание списка из входного потока
    s = sys.stdin.readlines()
    lst_in = [list(map(int, x.strip().split())) for x in s]

    # здесь продолжайте программу (используйте список lst_in)
    check_row = []
    n = 0
    index_i = []
    out = []
    for i in lst_in:
        # print(i)
        if sum(i) <= 1:
            check_row.append(1)
            n += 1
        else:
            check_row.append(0)
            n += 1
        for index, elem in enumerate(i):
            if elem == 1:
                index_i.append(index)

    print(index_i, check_row)
    inc = [1, -1]
    for index, elem in enumerate(check_row):
        if elem == 0:
            try:
                if (index_i[index] - index_i[index-1]) in inc or index_i[index+1] == index_i[index-1] or (index_i[index] - index_i[index+1]) in inc:
                    out.append("НЕТ")

                else:
                    out.append("ДА")
                    
            except IndexError:
                out.append("error")

    print(out)

    # print("ДА" if sum(check_row) >= 1 else "НЕТ")
    # or (index_i[index] - index_i[index+1]) == 1


    def tuples():
        numbers = (4, 7, 1, 9, 3)
        print(sum(numbers))

    tuples()


    def tuples2():
        values = (15, 8, 22, 1, 34, 10)
        print(f"Max: {max(values)}\nMin: {min(values)}")

    tuples2()

    def tuples3():
        tuple1 = (1, 2, 3)
        tuple2 = (4, 5, 6)

        print(tuple1 + tuple2)

    tuples3()

    def tuples4():
        fruits = ('apple', 'banana', 'cherry', 'orange')
        print("Yes we have it" if "banana" in fruits else "No we don't have it")
    tuples4()


    def tuples5():
        numbers = (1, 2, 3, 2, 4, 2, 5)
        print(numbers.count(2))
    tuples5()

    def tuples6():
        nums = (10, 20, 30, 40)
        nn = list(nums)
        nn[1] = 25
        print(tuple(nn))
    tuples6()

    def tuples7():
        colors = ('red', 'green', 'blue', 'yellow')
        cols = list(colors)
        cols[0] = colors[-1]
        cols[-1] = colors[0]
        print(tuple(cols))
    tuples7()

    def tuples8():
        words = ('hello', 'world', 'python')
        for word in words:
            if word == "world":
                for char in word:
                    print(char, end="")
                    if char == "r":
                        break
    tuples8()


    def dicts1():
        numbers = [1, 2, 3, 2, 4, 2, 5, 1, 3, 3]
        d = {}
        for elem in numbers:
            d.update({elem: numbers.count(elem)})
        print(d)
    dicts1()

    def dict2():
        dict1 = {'a': 100, 'b': 200}
        dict2 = {'b': 300, 'c': 400}

        for elem in dict2:

            if elem in dict1:
                a = dict1[elem] + dict2[elem]
                
                dict1.update({elem: a})

            else:
                a = dict2[elem]

                dict1.update({elem: a})

        print(dict1)
    dict2()


    def dict3():
        grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
        seq = []
        
        for name in grades:
            seq.append(grades[name])
            if grades[name] == max(seq):
                s = name
        print(s)
    dict3()


    def dict4():

        data = {'name': 'John', 'age': 25, 'city': 'New York'}
        for elem in data:
            if elem == "age":
                print(f"Ключ '{elem}' найден")

    dict4()

    def dict5():
        original = {'apple': 1, 'banana': 2, 'cherry': 3}
        d = {}
        for elem in original:
            d.update({original[elem]: elem})
        print(d)
    dict5()

    def dict6():
        products = {'apple': 50, 'banana': 30, 'cherry': 75, 'mango': 20}
        d = {}
        for elem in products:
            if products[elem] > 40:
                d.update({elem: products[elem]})
                
        print(d)
    dict6()

    def dict7():
        text = "hello world"
        d = {}
        for char in text:
            if char == " ":
                continue
            i = text.count(char)
            d.update({char: i})
        print(d)

    dict7()

    def dict8():
        keys = ['name', 'age', 'city']
        values = ['Alice', 25, 'New York']
        d = {}
        for k,v in zip(keys,values):
            d.update({k: v})
        print(d)
    dict8()

# built-in functions
    def task1():
        a = [10, 5, 8, 3, 1]
        print(f"Max: {max(a)}, Min: {min(a)}")
    task1()

    def task2():
        print("hello world".upper())
    task2()

    def task3():
        print(len(["apple", "banana", "cherry"]))
    task3()

    def task4(n):
        print(f"Square: {pow(n, 2)}")
    task4(int(input("Enter a number: ")))

    def task5(n):
        print("Yes" if n % 2 == 0 else "No")
    task5(int(input("Enter a number: ")))

    def task6(seq):
        print(f"Summary is: {sum(seq)}")
    task6(map(int, input("Enter a number: ").split()))

    def task7(n):
        x = lambda elem: elem * 2
        print(f"Amount is: {x(n)}")
    task7(int(input("Enter a number: ")))

    def task8():
        seq = [1, 2, 3, 4]
        out = []
        x = lambda elem: elem * 2
        for elem in seq:
            out.append(x(elem))
        print(out)
    task8()

    def task9():
        seq = [1, 2, 3, 4, 5, 6]
        x = lambda elem: elem % 2 == 0
        for elem in seq:
            if x(elem):
                continue
            else:
                seq.remove(elem)
        print(seq)
    task9()

    def task10(l):
        print(l)
    task10(task9())

    # lambda
    def lambda1():
        summ = lambda a, b: a + b
        print(f"Summary is: {summ(int(input("a: ")), int(input("b: ")))}")
    lambda1()

    def lambda2():
        check_even = lambda n: n % 2 == 0
        print("Yes" if check_even(int(input("n: "))) else "No")
    lambda2()

    def lambda3():
        len_str = lambda s: len(s)
        print(len_str(input()))
    lambda3()

    def lambda4():
        square = lambda i: i ** 2
        print(square(int(input())))
    lambda4()

    def lambda5(seq):
        x = lambda n: n % 2 == 0
        print(list(filter(x, seq)))
    lambda5([1, 4, 5, 8, 10, 13])

    def lambda6(seq):
        x = lambda s: sorted(s)
        print(x(seq))
    lambda6(['apple', 'banana', 'kiwi', 'cherry'])

    def lambda7(a, n):
        powed = lambda a, n: a ** n
        print(powed(a, n))
    lambda7(int(input()), int(input()))

    def lambda8(su):
        underscore = lambda s: s.replace(" ", "_")
        print(underscore(su))
    lambda8(input())

    def lambda9(seq):
        mx = lambda ls: max(ls)
        print(mx(seq))
    lambda9(map(int, input().split()))

    def lambda10(C):
        convert = lambda fl: fl * 9/5 + 32
        print(convert(C))
    lambda10(float(input("Celsius: ")))

    # list comprehensions

    def lc1():
        numbers = [1, 2, 3, 4, 5]
        print([x**2 for x in numbers])
    lc1()

    def lc2():
        numbers = [10, 15, 20, 25, 30, 35, 40]
        print([x for x in numbers if x % 2 == 0])
    lc2()

    def lc3():
        words = ["apple", "banana", "cherry", "kiwi"]
        print([len(word) for word in words])
    lc3()

    def lc4():
        words = ["car", "cat", "dog", "duck", "apple"]
        print([word for word in words if word.startswith("c")])
    lc4()

    def lc5():
        text = "hello world"
        vowels = ["a", "e", "i", "o", "u"]
        print([char if char not in vowels else '*' for char in text.lower()])
    lc5()

    def lc6():
        numbers = [5, 10, 15, 20, 25, 30, 35]
        print([elem for index, elem in enumerate(numbers) if index % 2 == 0])
    lc6()

    def lc7():
        sentence = "List comprehensions are powerful"
        print([word for word in sentence.split(" ")[::-1]])
    lc7()

    def lc8():
        n = range(1, 51)
        print([i for i in n if i % 3 == 0 and i % 5 == 0])
    lc8()

    def lc9():
        text = "abc123xyz45"
        print([elem for elem in text if elem.isdigit()])
    lc9()

    def lc10():
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        print([(elem1, elem2) for elem1, elem2 in zip(list1, list2)])
    lc10()

# recursion

    def rec1(n, i):
        if n > 121:
            rec1(int(input("oioi n is bigger 121: ")), 0)

        if n <= 121:
            i += 1
            n += 1
            print(f"Iteration {i}: {n}",end="\n")
            rec1(n, i) if n != 121 else print("\nYEEAH n is 121")
                    
    rec1(int(input("Enter a value of n: ")), 0)

    def rec2(n):
        if isinstance(n, str):
            i = 0
            for elem in n:
                i += int(elem)
            print(i)
        else:
            s = str(n)
            rec2(s)

    rec2(1234)

    lst = []
    def rec3(f):

        if len(lst) < f+2:
            lst.append(f)
            f = f-1
            rec3(f)
        else:
            i = 1
            for elem in lst:
                i *= elem
            print(i)

    rec3(5)

    class Car:
        def __init__(self, brand, model, year):
            self.brand = brand
            self.model = model
            self.year = year

        def display_info(self):
            print(f"Auto: {self.brand} {self.model}, Year: {self.year}")

    car = Car("Toyota", "Camry", 2020)
    car.display_info()

    class BankAcc:
        def __init__(self, owner_name, balance):
            self.owner_name = owner_name
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("oioi, your balance is less than withdraw - please make a deposit")

        def get_balance(self):
            print(f"Your balance is: {self.balance}")

    acc = BankAcc(input("Please enter your fullname: "),\
    int(input("Enter your current balance: ")))

    acc.deposit(500)
    acc.withdraw(200)

    acc.get_balance()

    class Rectangle:
        def __init__(self, w, h):
            self.w = w
            self.h = h
        
        def area(self):
            return self.w * self.h


        def perimetr(self):
            return (self.w + self.h) * 2

    rect = Rectangle(5, 10)
    print(f"Area: {rect.area()}\nP: {rect.perimetr()}")


    class Product:
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def total_cost(self):
            return (self.price * self.quantity)
        

    p1 = Product("Laptop", 1000, 3)
    p2 = Product("Phone", 500, 2)
    print(p1.total_cost() + p2.total_cost())

    class Book:
        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year

        def book_info(self):
            print(f"Book Title: {self.title}\n\
    Book Author: {self.author}\nYear: {self.year}")

    book = Book("1984", "George Orwell", 1949)
    book.book_info()


    def re_():
        import re
        text = "Мои контакты: alex@example.com, test.email@domain.net"

        a = re.findall(r'[\w\.]+@[\w\.]+', text)
        print(a)

    re_()

    def re_new():
        import re
        phone = "+123-456-7890"
        # phone = input()
        check = re.findall(r"\+\d{3}-\d{3}-\d{4}", phone)
        # print(check)
        print(True if check else False)
    re_new()

    def re_new2():
        import re
        text = "Сегодня 12/05/2023, а завтра будет 13/05/2023."
        dates = re.findall(r"\d{2}/\d{2}/\d{4}", text)
        print(dates)
    re_new2()

    def re_new3():
        import re
        text = "Hello world, regular expressions are fun!"
        print(re.sub(" ", "_", text))
    # Ожидаемый результат: "Hello_world,_regular_expressions_are_fun!"
    re_new3()

    def re_new4():
        import re
        text = "apple,orange.banana grape"
        new_text = re.findall(r"\w+", text)
        print(new_text)
        # Ожидаемый результат: ['apple', 'orange', 'banana', 'grape']
    re_new4()

    def re_new5():
        import re
        text = "Alice went to Wonderland. The White Rabbit was there."
        new_text = re.findall(r"[A-Z][\w]+", text)
        print(new_text)
    re_new5()

    def re_new6():
        import re
        text = "Order #1234, Price: $45.67"
        new_text = re.findall(r"[\d]", text)
        print("".join(new_text))
    re_new6()

    def re_new7():
        import re
        s = "Дата рождения: 15/07/1999"
        match = re.search(r"(\d{2})/(\d{2})/(\d{4})", s)

        if match:
            day = match.group(1)
            month = match.group(2)
            year = match.group(3)

        months = {
            "01": "January", "02": "February",
            "03": "March", "04": "April",
            "05": "May", "06": "June",
            "07": "July", "08": "August",
            "09": "September", "10": "October",
            "11": "November", "12": "December"
        }

        print(f"Day: {day}, \
    Month: {months[month]}, \
    Year: {year}")

    re_new7()

    def re_new8():
        import re
        text = "The quick Brown fox Jumped over the Lazy Dog."
        uppers = re.findall(r"[A-Z][a-z]+", text)
        print(uppers)
    re_new8()

    def re_new9():
        import re
        text = "Контакты: +123-456-7890, +987-654-3210, +555-123-4567"
        phones = re.findall(r"\+\d{3}-\d{3}-\d{4}", text)
        print(phones)

    re_new9()

    def re_new10():
        import re
        text = "Emails: alice@example.com, bob@domain.net, charlie@company.org"
        emails = re.findall(r"\w+@\w+\.\w+", text)
        print(emails)
    re_new10()

    def re_new11():
        import re
        text = "https://example.com"
        https = "https://"
        dotcomS = ".com"
        link = re.search(r"(\w+://)\w+(\.\w+$)", text)
        protocol = link.group(1)
        dotcom = link.group(2)
        print(True if protocol == https and dotcom == dotcomS else False)
    re_new11()

    def re_new12():
        import re
        s = "<h1>Welcome to my website</h1><h1>Enjoy your stay</h1>"
        text = re.findall(r"<h1>(.*?)</h1>", s)
        print(text)
    re_new12()

    def re_new13():
        import re
        s = "     "
        check = re.search(".+", s)
        # print(check)
        print(True if check != '' else False)
    re_new13()


    class Animal:
        def __init__(self, name, sound):
            self.name = name
            self.sound = sound

        def make_sound(self):
            print(f"{self.name} make sound {self.sound}")
        
    class Dog(Animal):
        def __init__(self, name, sound):
            super().__init__(name, sound)

    class Cat(Animal):
        def __init__(self, name, sound):
            super().__init__(name, sound)

    dog = Dog("Laika", "Woof")
    cat = Cat("Honey", "Meow")

    dog.make_sound()
    cat.make_sound()

    from math import pi, sqrt

    class Shape:
        def __init__(self, w, h):
            self.w = w
            self.h = h

        def area(self, out):
            print(f"{out:,.0f} m^2")

    class Rectangle(Shape):
        def __init__(self, w, h):
            super().__init__(w, h)

        def area(self):
            out = self.w * self.h
            return super().area(out)

    class Circle(Shape):
        def __init__(self, w, h):
            super().__init__(w, h)

        def area(self):
            s = self.w * self.h
            r = sqrt(s / pi)
            out = pi * pow(r, 2)
            return super().area(out)


    rectangle = Rectangle(100, 100)
    circle = Circle(50, 50)

    rectangle.area()
    circle.area()


    class Vehicle:
        def __init__(self, brand, speed, add_attr, s):
            self.brand = brand
            self.speed = speed
            self.add_attr = add_attr
            self.s = s

        def describe(self):
            return f"Brand: {self.brand},\nSpeed: {self.speed},\n" + f"{self.s} {self.add_attr}\n"

    class Car(Vehicle):
        def __init__(self, brand, speed, number_of_doors, s):
            s = "Number of doors:"
            number_of_doors = 4
            super().__init__(brand, speed, number_of_doors, s)

    class Bike(Vehicle):
        def __init__(self, brand, speed, type, s):
            s = "Type:"
            type = "for mountains"
            super().__init__(brand, speed, type, s)

    car = Car("Toyota", 120, number_of_doors="", s="")
    bike = Bike("Yamaha", 200, type="", s="")

    print(car.describe())
    print(bike.describe())

    class Polygon:
        def __init__(self, sides):
            self.sides = sides

        def display_info(self):
            if self.sides > 4:
                return f"This polygon has {self.sides} sides"
            elif self.sides == 4:
                return f"It is square, it has {self.sides} sides"
            elif self.sides == 3:
                return f"It is triangle, it has {self.sides} sides"
            else:
                return f"It is not a figure"

    class Triangle(Polygon):
        def __init__(self, sides):
            super().__init__(sides)

    class Square(Polygon):
        def __init__(self, sides):
            super().__init__(sides)


    tri = Triangle(int(input("Enter a quantity of sides: ")))
    sq = Square(int(input("Enter a quantity of sides: ")))

    print(tri.display_info())
    print(sq.display_info())