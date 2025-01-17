def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    try:
        if "/" in fraction:
            fraction = fraction.split("/", -1)
        else:
            raise ValueError

        x = fraction[0]
        y = fraction[1]
        if (x and y).isdigit():

                if int(y) == 0:
                    raise ZeroDivisionError

                form = round((int(x) / int(y)) * 100)

                if form > 100:
                    raise ValueError
                else:
                    return form      
        else:
            raise ValueError

    except ZeroDivisionError:
        raise
    except ValueError:
        raise


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
