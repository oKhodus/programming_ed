import emoji as em

def main(user_inp):
    print(em.emojize(f"Output: {user_inp}", language='alias'))
main(input("Input: "))
