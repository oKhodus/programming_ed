def main():
    inp = input("What is the Answer to the Great Question of Life, the Universe, and Everything?: ").lower().strip()
    fortyTwo_statemant = {"forty-two", "forty two", "42", 42}
    if inp in fortyTwo_statemant:
        print("Yes")
    else:
        print("No")
main()
