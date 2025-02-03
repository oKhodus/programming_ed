import re

def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"(^|\W)um($|\W)", s, re.IGNORECASE)
    return len(um) if um else 0

if __name__ == "__main__":
    main()
