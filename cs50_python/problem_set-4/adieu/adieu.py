import inflect as INF


def variant_without_INF():
    ls = []
    while True:
        try:
            user_inp = input("Name: ")
            ls.append(user_inp.capitalize())

        except EOFError:
            fstr = 'Adieu, adieu, to '
            for name in ls:
                if name != ls[-1]:
                    if len(ls) <= 2:
                        fstr += f"{name} "
                    else:
                        fstr += f"{name}, "
                elif len(ls) > 1 and name == ls[-1]:
                    fstr += f"and {name}"
                elif len(ls) == 1:
                    fstr += f"{name}"
            print(fstr)
            exit()


def variant_with_INF():
    ls = []
    inflect = INF.engine()
    while True:
        try:
            user_inp = input("Name: ")
            ls.append(user_inp.capitalize())

        except EOFError:
            fstr = 'Adieu, adieu, to ' + inflect.join(ls)
            print(fstr)
            exit()
    

def main():
    choose = int(input("Enter a number of variant (1-2): "))
    variant_without_INF() if choose == 1 else variant_with_INF()


if __name__ == "__main__":
    main()