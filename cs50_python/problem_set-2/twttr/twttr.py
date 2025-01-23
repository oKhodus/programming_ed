def find_character(word):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    total_word = ""
    for char in word:
        if char not in vowels:
            total_word += char
            
    print(f"Output: {total_word.strip()}")
find_character(input("Input: "))
