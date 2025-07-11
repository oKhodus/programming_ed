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


# print(imple_arr())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add_head(self, node):
        node.next = self.head
        self.head = node

    def add_tail(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node    
    
    def add_after(self, target, new_node):
        if self.head is None:
            raise Exception('List is empty')
        for node in self:
            if node.data == target:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception(f'Node with data {target} not found')
    
    def add_before(self, target, new_node):
        if not self.head:
            return Exception('List is empty')
        if self.head.data == target:
            return self.add_head(new_node)
        
        prev = self.head
        for node in self:
            if node.data == target:
                prev.next = new_node
                new_node.next = node
                return
            prev = node
        raise Exception(f'Node with data {target} not found')
    
    def remove_node(self, target):
        if not self.head:
            return Exception('List is empty')
        
        if self.head.data == target:
            self.head = self.head.next
            return
        
        prev = self.head
        for node in self:
            if node.data == target:
                prev.next = node.next
                return
            prev = node
        raise Exception(f'Node with data {target} not found')

ll = LinkedList()

ll.add_head(Node('a'))
ll.add_head(Node('b'))
ll.add_head(Node('c'))
ll.add_tail(Node('z'))
ll.add_tail(Node('x'))
ll.add_tail(Node('y'))

ll.add_after('c', Node('afterC'))
ll.add_before('b', Node('beforeB'))
ll.remove_node('z')

print(ll)