"""
Find the kth Node from END of link list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
    
    def add_ll(self, node):
        if self.head is None:
            self.head=node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next=node

    def printll(self):
        temp = self.head
        while temp:
            print(temp.data," --> ", end="")
            temp = temp.next
        print("\n")
    
    def find_kth_node_from_end(self, kth_node):
        # find the total lengh of LL
        temp = self.head
        total_lenght = 0
        while temp:
            total_lenght += 1
            temp = temp.next
        if total_lenght and total_lenght >= kth_node:
            kth_node_start_node = total_lenght - kth_node
            count = 0
            temp = self.head
            while temp:
                if kth_node_start_node == count:
                    print("kth Node from End", temp.data)
                temp = temp.next
                count += 1
        
        else:
            print("Kth Node from END is not found")


if __name__ == "__main__":
    ll = LinkList()
    ll.add_ll(Node(3))
    ll.add_ll(Node(4))
    ll.add_ll(Node(5))
    ll.add_ll(Node(6))
    ll.add_ll(Node(7))
    ll.printll()
    ll.find_kth_node_from_end(1)
