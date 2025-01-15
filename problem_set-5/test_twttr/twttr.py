def main():
    print(shorten(input("Input: ")))


def shorten(word):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    total_word = ""
    for char in word:
        if char not in vowels:
            total_word += char

    return total_word.strip()


if __name__ == "__main__":
    main()
