class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

##############################################################################

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    ##############################################################################
    '''Adding Node at the end of the list
    '''
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node
            new_node.prev = ptr
            new_node.next = None

    ############################################################
    '''Adding Node at the start of the list
    '''
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    ##############################################################################
    '''Deleting nodes at various places
    '''
    def delete(self, key):
        ptr = self.head
        while ptr:

            # Removing first node by splitting it in two cases
            #----------------------------------------------------------------

            if ptr.data == key and ptr == self.head:
                # Case 1(Remove First and only node of the list)
                if not ptr.next:
                    ptr = None
                    self.head = None
                    return

                # Case 2(Remove first node of list having many nodes):
                else:
                    nxt = ptr.next
                    ptr.next = None
                    nxt.prev = None
                    ptr = None
                    self.head = nxt
                    return

            #----------------------------------------------------------------

            elif ptr.data == key:
                # Case 3(Removing middle nodes)
                if ptr.next:
                    nxt = ptr.next
                    prev = ptr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    ptr.next = None
                    ptr.prev = None
                    ptr = None
                    return

                # Case 4 (Remove last node of the list)
                else:
                    prev = ptr.prev
                    prev.next = None
                    ptr.prev = None
                    ptr = None
                    return
            ptr = ptr.next

    ##############################################################################
    '''Adding node to a specific position
    '''
    def insert(self, key, data):
        ptr = self.head
        while ptr:
            if ptr.prev is None and ptr.data == key:
                self.prepend(data)
                return
            elif ptr.data == key:
                new_node = Node(data)
                prev = ptr.prev
                prev.next = new_node
                ptr.prev = new_node
                new_node.next = ptr
                new_node.prev = prev
            ptr = ptr.next

    ##############################################################################
    '''Display all elements of the list
    '''
    def display(self):
        elements = []
        ptr = self.head
        while ptr:
            elements.append(ptr.data)
            ptr = ptr.next
        return elements


##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################

'''Testing'''


p = DoublyLinkedList()
p.append(96)
p.append(14)
p.append(75)
p.append(9)
print(*p.display(),sep=" ↔ ",end=" → Null \n")
p.insert(96,23)
print(*p.display(),sep=" ↔ ",end=" → Null \n")
p.delete(23)
print(*p.display(),sep=" ↔ ",end=" → Null \n")
p.prepend(23)
p.prepend(54)
print(*p.display(),sep=" ↔ ",end=" → Null \n")