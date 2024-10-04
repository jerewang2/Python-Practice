class Node(object):

    def __init__(self, value, next = None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

def main():
    # Creating a linked list
    Head = Node(1)
    a = Node(2)
    b = Node(3)
    c = Node(7)

    Head.next = a
    a.next = b
    b.next = c

    print(f'Node head value: {Head.value}')
    print(f'Next node of head: {Head.next.value}')
    print(f'Node a value: {a.value}')
    print(f'Next node of a: {a.next.value}')
    print(f'Node b value: {b.value}')
    print(f'Next node of b: {b.next.value}')
    print(f'Node c value: {c.value}')

    # Traversing a linked list O(n) time complexity
    curr = Head
    while curr:
        print(curr)
        curr = curr.next

    # Display linked list O(n) time complexity
    def display(head):
        curr = head
        elements = []
        while curr:
            elements.append(str(curr.value))
            curr = curr.next
        print(' -> '.join(elements))
    
    # Search for node value O(n) time complexity
    def search(head, val):
        curr = head
        while curr:
            if val == curr.value:
                return True
            else:
                curr = curr.next
        return False

    display(Head)
    print(search(Head, 7))

if __name__ == "__main__":
    main()
