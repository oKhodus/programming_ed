
def count_sheep(n):
    if n < 1: return ""
    out = ''
    for elem in range(1, n+1):
        out += f"{elem} sheep..."
    return out

print(
    count_sheep(int(input('enter: ')))
)

def find_multiples(n, lim):
    if n < 0: return ""
    if lim <= n: return ""

    out = []
    for m in range(n, lim+1, n):
        out.append(m)
    return out

print(
    find_multiples(5, 25)
)

def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    condC = a + b > c
    condB = a + c > b
    condA = b + c > a

    return True if condC and condB and condA else False

print(is_triangle(7, 2, 2))

def high_and_low(numbers):
    arr = []
    s = numbers.split(" ")
    for elem in s:
        if elem != " ":
            arr.append(int(elem))

    return f"{max(arr)} {min(arr)}"

print(high_and_low(("8 3 -5 42 -1 0 0 -9 4 7 4 -4")))


def sum_str(a, b):

    if a == "" and b == "": return "0"
    
    if b == '': b = 0
    if a == '': a = 0

    a, b = int(a), int(b)
    return f"{a + b}"
    

print(sum_str("", ""))


def order(sentence):
    arr = sentence.split()
    result = [''] * len(arr)

    for word in arr:
        for char in word:
            if char.isdigit():
                index = int(char) - 1
                result[index] = word

    return ' '.join(result)


order(
    'g3ood 4of the2 pe6ople th5eFo1r '
)

def rps(p1, p2):
    mes1, mes2 = "Player 1 won!", "Player 2 won!"

    
    cond_p1 = [
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock")]

    if p1 == p2:
        return "Draw!"

    return mes1 if (p1, p2) in cond_p1 else mes2

print(rps("paper","rock"))



def sort_array(source_array):
    odds = []
    for x in source_array:
        if x % 2 != 0:
            odds.append(x)

    odds.sort()

    out = []
    odd_index = 0

    for x in source_array:
        if x % 2 == 0:
            out.append(x)
        else:
            out.append(odds[odd_index])
            odd_index += 1

    return out


""" 
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

def solution(text, ending):
    return True if text.endswith(ending) else False 

print(
    
solution("abc", "bc")
)

def abbrev_name(name):
    elems = name.split()
    return f"{elems[0][0].upper()}.{elems[1][0].upper()}"

print(
    abbrev_name("Sam Harris")
)

def add_binary(a,b):
    res = bin(a + b)
    return res[2:]

print(
    add_binary(51, 12)
)


def remove_every_other(my_list):
    out = []
    for index, elem in enumerate(my_list):
        if index % 2 == 0:
            out.append(elem)
    return out


print(
    remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
)