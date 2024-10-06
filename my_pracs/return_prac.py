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
