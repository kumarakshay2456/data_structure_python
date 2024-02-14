"""
Find the mid element is LinkList

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self) -> None:
        self.head = None
    
    def add_element(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
    
    def printll(self):
        temp = self.head
        while temp:
            print(temp.data, end = "")
            if temp.next:
                print(" --> ", end="")
            temp = temp.next
        print("\n")

    
    def find_middle_element_ll(self):
        slow = self.head
        fast = self.head
        if slow == None or fast== None:
            print("Mid element is not exits")
            return
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Mid element is", slow.data)


if __name__=='__main__':
    ll = LinkList()
    print(Node(2))
    ll.add_element(Node(2))
    ll.add_element(Node(3))
    ll.add_element(Node(4))
    ll.add_element(Node(5))
    ll.add_element(Node(6))
    ll.add_element(Node(7))
    ll.add_element(Node(8))
    ll.printll()
    ll.find_middle_element_ll()
