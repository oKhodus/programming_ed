def is_valid(s):
    if not (6 >= len(s) >= 2):
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False

    found_dig = False

    for char in s:
        if char.isdigit():
            if char == "0" and not found_dig:
                return False
            found_dig = True
        elif found_dig:
            return False
    return True

def main():
    inp = input("Plate: ")
    if is_valid(inp):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()