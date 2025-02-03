import validators


def main():
    print(check(input("What's your email address? ")))


def check(email):
    return f"Valid" if validators.email(email) == True else f"Invalid"


if __name__ == "__main__":
    main()
