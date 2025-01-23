import random as RAN


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level)
        correct_answer = x + y
        tries = 0

        while tries < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            tries += 1
        if tries == 3:
            print(correct_answer)
    print(f"Score: {score}")


def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            n = int(input("Level: "))

            if n in levels:
                return n
        except ValueError:
            pass

def generate_integer(level):
    ranges = {
        1: (0, 9),
        2: (10, 99),
        3: (100, 999)
    }
    if level in ranges:
        low, high = ranges[level]
        return RAN.randint(low, high), RAN.randint(low, high)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
