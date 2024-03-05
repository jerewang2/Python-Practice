class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.nextnode = b
    b.nextnode = c

    print(f'Node a value: {a.value}')
    print(f'Next node of a: {a.nextnode.value}')
    print(f'Node b value: {b.value}')
    print(f'Next node of b: {b.nextnode.value}')
    print(f'Node c value: {c.value}')

if __name__ == "__main__":
    main()
