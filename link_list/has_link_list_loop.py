class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkList:
    def __init__(self) -> None:
        self.head = None
    
    def add_ll(self, node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
    
    def make_ll_loop(self, value):
        temp = self.head
        middle_element = None
        while temp.next:
            if value == temp.data:
                middle_element = temp
            temp = temp.next
        temp.next = middle_element
    
    def find_ll_loop(self):
        slow_pointer, fast_pointer = self.head, self.head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                print("Loop is found")
                return 1
        print("Loop is not found")
        return 0





    
    def print__ll(self):
        temp = self.head
        while temp:
            if temp.next:
                print(temp.data, " --> ", end="")
            else:
                print(temp.data)
            temp = temp.next
        print("\n")
    

if __name__ == "__main__":
    ll = LinkList()
    ll.add_ll(Node(2))
    ll.add_ll(Node(3))
    ll.add_ll(Node(4))
    ll.add_ll(Node(5))
    ll.add_ll(Node(6))
    ll.add_ll(Node(7))
    ll.add_ll(Node(9))
    ll.print__ll()
    ll.make_ll_loop(4)
    # ll.print__ll()
    ll.find_ll_loop()






