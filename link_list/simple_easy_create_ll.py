# Another Shortcut way to add the data in linkList

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    print(head.val)
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Example usage:
# Constructing a linked list: 8 -> 4 -> 5
head = ListNode(8, ListNode(4, ListNode(5)))

# Print the linked list values
print_linked_list(head)