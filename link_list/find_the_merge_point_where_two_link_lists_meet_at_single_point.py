"""
Suppose there are two Single Link List and both of which merge same point and become single linklist.
Need to find the node at which they merge.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:

    def __init__(self) -> None:
        self.head2 = None
        self.head1 = None
    
    def add_link_list_1(self, node):
        if self.head1 == None:
            self.head1 = node
        else:
            temp = self.head1
            while temp.next:
                temp = temp.next
            temp.next = node

    def printll_1(self):
        temp = self.head1
        while temp:
            if temp.next:
                print(temp.data, "-->", end="")
            else:
                print(temp.data)
            temp = temp.next
        
        print("\n")
    
    def add_link_list_2(self, node):
        if self.head2 == None:
            self.head2 = node
        else:
            temp = self.head2
            while temp.next:
                temp = temp.next
            temp.next = node    

    def printll_2(self):
        temp = self.head2
        while temp:
            if temp.next:
                print(temp.data, "-->", end="")
            else:
                print(temp.data)   
            temp = temp.next
        print("\n")


    # Assumming that headA and headB has two diffrent link list and one intersection Node
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # find the total lenght of the both list
        lengthA = 0
        tempA = headA
        while tempA:
            lengthA += 1
            tempA = tempA.next
        lengthB = 0
        tempB = headB
        while tempB:
            lengthB += 1
            tempB = tempB.next
        diffA = 0
        diffB = 0
        if lengthA > lengthB:
            diffA = lengthA - lengthB
        else:
            diffB = lengthB - lengthA
        if diffA > 0:
            count = 0
            while diffA != count:
                headA = headA.next
                count += 1
        else:
            count = 0
            while diffB!= count:
                headB = headB.next
                count += 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        if headA or headB:
            return headA
        return None



if __name__ == "__main__":
    ll = LinkList()
    ll.add_link_list_1(Node(2))
    ll.add_link_list_1(Node(3))
    ll.add_link_list_1(Node(4))
    ll.add_link_list_1(Node(5))
    ll.add_link_list_1(Node(6))
    ll.add_link_list_1(Node(9))
    ll.printll_1()
    ll.add_link_list_2(Node(4))
    ll.add_link_list_2(Node(5))
    ll.add_link_list_2(Node(6))
    ll.add_link_list_2(Node(7))
    ll.add_link_list_2(Node(8))
    ll.add_link_list_2(Node(9))
    ll.printll_2()




