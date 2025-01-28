import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    valid = r"(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
    return True if re.match(rf"^{valid}\.{valid}\.{valid}\.{valid}$", ip) else False


if __name__ == "__main__":
    main()
