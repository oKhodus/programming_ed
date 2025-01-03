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