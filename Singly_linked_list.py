class Node:

    def __init__(self, input_data=None):
        self.data = input_data
        self.next = None

##############################################################################

class Singly_linked_list:

    def __init__(self):
        self.head = Node()

    ##############################################################################

    '''Append() instance which inserts a node
        at the end of the list
    '''

    def append(self, data):
        new_node = Node(data)
        ptr = self.head
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = new_node

    ##############################################################################

    '''display instance which gives 
       all the elements of the list in form
       of 'list' data type
    '''

    def display(self):
        if self.head == None:
            return "Underflow"
        else:
            elements = []
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
                elements.append(ptr.data)
            return elements

    ##############################################################################

    '''Get() instance which gives the node data
        of the required index
    '''

    def get(self, index):
        elements = Singly_linked_list.display(self)
        if index > self.length() - 1 or index <= 0:
            return "Index out of range !"
        else:
            return elements[index]

    ##############################################################################

    '''Length instance which gives the current length
        of the list 
    '''

    def length(self):
        pointer = self.head
        length_of_list = 0
        while pointer.next != None:
            length_of_list += 1
            pointer = pointer.next
        return length_of_list

    ##############################################################################

    '''Insert() instance to insert new node at given index
        which includes both start and end of list
    '''

    def insert(self, index, data):
        ptr = self.head
        if ptr == None:
            return "Empty list"
        elif index > self.length() - 1 or index == None:
            self.append(data)
            return None
        elif index <= 0:
            new_node = Node(data)
            new_node.next = self.head.next
            self.head.next = new_node
        else:
            new_node = Node(data)
            ptr = self.head
            cur_idx = 0
            while cur_idx <= index:
                if cur_idx == index:
                    new_node.next = ptr.next
                    ptr.next = new_node
                ptr = ptr.next
                cur_idx += 1

    ##############################################################################

    '''Erase() instance to delete  node at given index
       which includes both start and end of list
    '''

    def erase(self, index):
        if self.length() == 0 or index >= self.length():
            return "'Erase' Index out of range!"
        cur_idx = 0
        ptr = self.head
        while True:
            last_node = ptr
            ptr = ptr.next
            if cur_idx == index:
                last_node.next = ptr.next
                return
            cur_idx += 1


##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################

'''Testing'''

p = Singly_linked_list()
p.append(94)
p.append(54)
p.append(69)
p.append(75)
print(*p.display(), sep="->", end="->Null\n")
print(p.get(5))
print(p.length())
print(p.get(2))
p.insert(0, 60)
print(p.length())
print(*p.display(), sep="->", end="->Null\n")
p.insert(0, 36)
print(*p.display(), sep="->", end="->Null\n")
p.erase(2)
print(*p.display(), sep="->", end="->Null\n")