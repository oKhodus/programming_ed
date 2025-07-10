from random import randint
from array import array

def imple_arr():
    random_ls = [x for x in range(1, randint(5, 10))]
    put_to_arr = max(random_ls) + 100
    arr = array('d', random_ls)

    """elem added to the tail (end) of arr"""
    arr.append(put_to_arr)


    """group of elems added to the tail (end) of arr"""
    ext = [x for x in range(200, randint(201, 210))]
    arr.extend(ext)


    """elem which wanna insert and its position"""
    myInsertion = 10405
    pos = 0
    arr.insert(pos, myInsertion) 

    concated = arr + arr

    wasPopped = arr.pop()

    arr.remove(myInsertion)

    def find_pos():
        for index, elem in enumerate(arr):
            if elem > 10:
                return index

    sliced = arr[:find_pos()]

    return f"\nCurrent length of array is: {len(arr)}\n\
New max elem, added to arr: {put_to_arr}\n\
New elems which were extended: {ext}\n\
My elem which wanna insert: {myInsertion}, and position: {pos}\n\
cancated also will be: {concated}\n\
Elem which was popped: {wasPopped}\n\
Was removed: {myInsertion}\n\
Sliced array where integers <= 10: {sliced}\n\
    \nFinal array: {arr}"


print(imple_arr())