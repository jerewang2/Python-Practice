# Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle." A cycle is when a node's next point actually points back to a previous node in the list.

class Node(object):
    
    def __init__(self, value):
        
        self.value = value
        self.nextnode = None

def cycle_check(node):
    
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:
        
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True

    return False


def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    d.nextnode = a

    print(cycle_check(a))

if __name__ == "__main__":
    main()
