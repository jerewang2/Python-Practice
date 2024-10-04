class DoublyLinkedLists(object):

    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
    
    def __str__(self):
        return str(self.value)

def main_1():
    head = tail = DoublyLinkedLists(1)
    a = DoublyLinkedLists(2)
    b = DoublyLinkedLists(3)
    c = DoublyLinkedLists(4)

    a.next_node = b
    b.prev_node = a
    
    b.next_node = c
    c.prev_node = b

    print(f'Node a: {a.value} | Next Node a: {a.next_node.value}')
    print(f'Node b: {b.value} | Prev Node b: {b.prev_node.value} | Next Node b: {b.next_node.value}')
    print(f'Node c: {c.value} | Prev Node c: {c.prev_node.value}')

    
class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

def main():
    head = tail = DoublyNode(1)
    print(tail)

    def display(head):
        curr = head
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(' <-> '.join(elements))
    
    display(head)

    def insert_at_beginning(head, tail, val):
        new_node = DoublyNode(val, next = head)
        head.prev = new_node
        return new_node, tail

    def insert_at_end(head, tail, val):
        new_node = DoublyNode(val, prev = tail)
        tail.next = new_node
        return head, new_node

    head, tail = insert_at_beginning(head, tail, 3)
    display(head)

    head, tail = insert_at_end(head, tail, 7)
    display(head)


if __name__ == '__main__':
    main()
