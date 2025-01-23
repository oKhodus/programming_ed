import random as R

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n >= 1:
                break
        except ValueError:
            pass

    r_val = R.randint(1, n)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            if guess < r_val:
                print("Too small!")
            elif guess > r_val:
                print("Too large!")
            else:
                print("Just right!")
                exit()
        except ValueError:
            pass
main()
