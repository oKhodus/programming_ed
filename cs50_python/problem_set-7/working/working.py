import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    with_minutes = (
        r"([1-9]|1[0-2]):([0-5][0-9]) (AM|PM) to ([1-9]|1[0-2]):([0-5][0-9]) (AM|PM)"
    )

    without_minutes = r"([1-9]|1[0-2]) (AM|PM) to ([1-9]|1[0-2]) (AM|PM)"

    mixed_1 = r"([1-9]|1[0-2]) (AM|PM) to ([1-9]|1[0-2]):([0-5][0-9]) (AM|PM)"
    mixed_2 = r"([1-9]|1[0-2]):([0-5][0-9]) (AM|PM) to ([1-9]|1[0-2]) (AM|PM)"

    time = (
        re.findall(with_minutes, s)
        or re.findall(without_minutes, s)
        or re.findall(mixed_1, s)
        or re.findall(mixed_2, s)
    )

    if not time:
        return ValueError

    if len(time[0]) == 4:
        from_hour, from_period, to_hour, to_period = time[0]
        from_min, to_min = "00", "00"
    elif len(time[0]) == 5:
        if ":" in s.split(" to ")[0]:
            from_hour, from_min, from_period, to_hour, to_period = time[0]
            to_min = "00"
        else:
            from_hour, from_period, to_hour, to_min, to_period = time[0]
            from_min = "00"
    else:
        from_hour, from_min, from_period, to_hour, to_min, to_period = time[0]

    def to_24h(hour, minute, period):
        hour = int(hour)
        if period == "PM" and hour != 12:
            hour += 12
        if period == "AM" and hour == 12:
            hour = 0
        return f"{hour:02}:{minute}"

    from_t = to_24h(from_hour, from_min, from_period)
    to_t = to_24h(to_hour, to_min, to_period)

    return f"{from_t} to {to_t}"


if __name__ == "__main__":
    main()
