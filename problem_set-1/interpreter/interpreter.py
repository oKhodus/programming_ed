def main():
    inp = input("Expression: ")
    x, y, z = inp.split(" ")
    int_X = float(x)
    int_Z = float(z)
    if y == "+":
        print(int_X + int_Z)
    elif y == "-":
        print(int_X - int_Z)
    elif y == "*":
        print(int_X * int_Z)
    elif y == "/":
        print(int_X / int_Z)
    else:
        print(f"Sorry {y} is not a correct value.")
main()
