class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:

    def __init__(self):
        self.head = None

    def printll(self):
        temp = self.head
        while temp:
            print("TEMP {0}".format(temp.data))
            temp = temp.next


if __name__ == "__main__":
    llist = LinkList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.printll()
