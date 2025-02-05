from datetime import date
import re
import inflect
import sys


def main():
    p = inflect.engine()
    today = date.today().isoformat()
    inp = input("Date of Birth: ")
    birthday = birth(inp)
    if birthday == "Invalid date":
        sys.exit("Invalid date")
    print(f"{p.number_to_words(calc(birthday, today)).capitalize()} minutes")


def calc(birth, today):

    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", birth):
        raise ValueError
        
    birth_ls = birth.split("-")
    today_ls = today.split("-")
    diff = []
    for elem_birth, elem_today in zip(birth_ls, today_ls):
        diff.append(int(elem_today) - int(elem_birth))
    y, m, d = diff
    minutes = (d * 1440) + (m * 43800) + (y * 525600)
    return minutes


def birth(s):
    match = re.match(
        r"(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])", s
    )
    if match:
        year, month, day = match.groups()
        days_in_month = [
            31,
            28 + (1 if int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0) else 0),
            31, 30, 31, 30, 31, 31, 30, 31, 30, 31,
        ]
        if int(day) > days_in_month[int(month) - 1]:
            raise ValueError("Invalid date")
        return match.group(0)
    raise ValueError("Invalid date")


# YYYY-MM-DD


if __name__ == "__main__":
    main()
