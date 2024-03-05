class DoublyLinkedLists(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

def main():
    a = DoublyLinkedLists(1)
    b = DoublyLinkedLists(2)
    c = DoublyLinkedLists(3)

    a.next_node = b
    b.prev_node = a
    
    b.next_node = c
    c.prev_node = b

    print(f'Node a: {a.value} | Next Node a: {a.next_node.value}')
    print(f'Node b: {b.value} | Prev Node b: {b.prev_node.value} | Next Node b: {b.next_node.value}')
    print(f'Node c: {c.value} | Prev Node c: {c.prev_node.value}')

if __name__ == '__main__':
    main()
