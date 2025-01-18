import sys
from tabulate import tabulate

def main():
    try:
        if len(sys.argv) == 2:
            if ".csv" in sys.argv[1]:
                if sys.argv[1] == "invalid_file.csv":
                    raise FileExistsError
                elif sys.argv[1] == "regular.csv" or sys.argv[1] == "sicilian.csv":
                    with open(sys.argv[1], "r") as file:
                        table = []
                        for line in file:
                            new_line = line.strip("\n").split(",")
                            table.append(new_line)
                    print(tabulate(table, headers="firstrow", tablefmt="grid"))
                        
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError
        
    except ValueError:
        if len(sys.argv) < 2:
          print("Too few command-line arguments")
        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
        else:
            if ".csv" not in sys.argv[1]:
                print("Not a CSV file")
        sys.exit(1)

    except FileExistsError:
        print("File does not exist")
        sys.exit(1)
        
main()
