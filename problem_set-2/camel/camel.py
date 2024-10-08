def case_converter():
    camel_case = input("camelCase: ")
    snake_case = ""
    for letter in camel_case:
        if letter.isupper():
            snake_case += "_" + letter.lower()
        else:
            snake_case += letter
    print(f"snake_case: {snake_case}")

case_converter()


#  Anti-converter
# def case_converter():
#     snake_case = input("snake_case: ")
#     camel_case = ""
#     for letter in snake_case:
#         if letter.__contains__("_"):
#             camel_case += letter.replace("_", letter).capitalize()
#         else:
#             camel_case += letter
#     print(f"camel_case: {camel_case}")
#
# case_converter()