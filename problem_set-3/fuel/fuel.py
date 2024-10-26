def fuel(f):
    try:
        if "/" in f:
            f = f.split("/", -1)
        else:
            raise ValueError

        x = f[0]
        y = f[1]
        
        if (x and y).isdigit():

            if int(y) == 0:
                raise ZeroDivisionError

            form = round((int(x) / int(y)) * 100)

            if form > 100:
                raise ValueError


            if form >= 99:
                print("F")
            elif form <= 1:
                print("E")
            else:
                print(f"{form}%")
        else:
            raise ValueError

    except ZeroDivisionError:
        fuel(input("Fraction: "))
    except ValueError:
        fuel(input("Fraction: "))
fuel(input("Fraction: "))
