def taq():
      try:
            total = 0
            items = {"Baja Taco": 4.25,
                 "Burrito": 7.50,
                 "Bowl": 8.50,
                 "Nachos": 11.00,
                 "Quesadilla": 8.50,
                 "Super Burrito": 8.50,
                 "Super Quesadilla": 9.50,
                 "Taco": 3.00,
                 "Tortilla Salad": 8.00}
            while True:

                  inp = input("Item: ").title()

                  if inp in items:
                        total += items.get(inp)
                        print(f"Total: ${total:.2f}")
                  else:
                        taq()


      except EOFError:
            pass

taq()
