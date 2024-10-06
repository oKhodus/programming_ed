def greeting(greet):
    str_greet = f"{greet}"
    return str_greet


def main():
    inp = greeting(input("Greeting: ").lower().strip())
    if "hello" in inp:
        print("$0")
    elif inp.startswith("h") and "hello" not in inp:
        print("$20")
    else:
        print("$100")
main()
