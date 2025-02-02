import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    without_minutes = r"[1][0-2]|[1-9]|[1][0-2] AM to [1][0-2]|[0-9] PM"
    time = re.findall(rf"{without_minutes}", s)
    # |[1-9]:[0-5][0-9]

    return time


if __name__ == "__main__":
    main()
