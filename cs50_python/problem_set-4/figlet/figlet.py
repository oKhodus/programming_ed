from pyfiglet import Figlet
import sys

def main():

    try:
        figger = Figlet()
        fonts = figger.getFonts()

        if len(sys.argv) == 3 and \
        (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
            if sys.argv[2] in fonts:
                user_input = input("Input: ")
                figger.setFont(font=sys.argv[2])
            else:
                raise ValueError

        elif len(sys.argv) > 1 and (sys.argv[1] != "-f" or sys.argv[1] != "--font"):
            raise ValueError

        else:
            user_input = input("Input: ")
            figger.setFont(font='slant')


        print(figger.renderText(user_input))

    except ValueError:
        sys.exit(1)
    except IndexError:
        sys.exit(1)

main()
