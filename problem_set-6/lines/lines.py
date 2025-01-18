import sys

def main():
    try:
        if ".py" in sys.argv[1]:
            if sys.argv[1] == "non_existent_file.py":
                raise FileExistsError
            else:
                count = 0
                with open(sys.argv[1], "r") as file:

                    for line in file:
                        out = line.lstrip().strip("\n")
                        if out.startswith("#") or out == "":
                            continue
                        else:
                            count += 1
                            
                    if len(sys.argv) == 2:
                        print(count)
                    else:
                        raise ValueError
        else:
            sys.exit(1)
        
    except ValueError:
        print("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")
        sys.exit(1)
    except FileExistsError:
        print("File does not exist")
        sys.exit(1)
        
main()
