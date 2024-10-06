def main():
    out = ["breakfast time", "lunch time", "dinner time"]
    inp = input("What time is it? ")
    conv_inp = convert(inp)
    if 7 <= conv_inp <= 8:
        print(out[0])
    elif 12 <= conv_inp <= 13:
        print(out[1])
    elif 18 <= conv_inp <= 19:
        print(out[2])
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    conv_hours = float(hours)
    conv_minutes = int(minutes)
    decimal_time = conv_hours + conv_minutes / 60
    return decimal_time




if __name__ == "__main__":
    main()
