"""
Reverse Link List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
    
    def insert_last_of_ll(self, node):
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = node
    
    def printll(self):
        temp = self.head
        while temp:
            print("Lint List is -> ",temp.data)
            temp = temp.next
    
    def reversell(self):
        prev_ptr = None
        temp = self.head
        while temp:
            next_ptr = temp.next
            temp.next = prev_ptr
            prev_ptr = temp
            temp = next_ptr
        self.head = prev_ptr






        


if __name__== "__main__":
    ll = LinkList()
    ll.insert_last_of_ll(Node(1))
    ll.insert_last_of_ll(Node(2))
    ll.insert_last_of_ll(Node(3))
    print("Before reverse the link link")
    ll.printll()
    ll.reversell()
    print("After the reverse the link list")
    ll.printll()
    print("Again Correcting the link link")
    ll.reversell()
    ll.printll()



    
