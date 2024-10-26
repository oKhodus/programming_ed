from collections import Counter as c

def groc():
    list_of_items = []

    while True:

        try: 
            item = input()
            list_of_items.append(item)
                   
        except EOFError:
            break
    
    list_of_items.sort()
    summary = c(list_of_items)

    for item, count in summary.items():
        print(f"{count} {item.upper()}") 
            

groc()