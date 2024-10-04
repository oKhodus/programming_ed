def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

def main():
    inp = input()
    converted_str = convert(inp)
    print(converted_str)
main()
