class Queue:

    def __init__(self, acapacity):
        self.items = []
        self.capacity = acapacity
        self.head = 0
        self.tail = 0

    def size(self):
        return len(self.items)

    def isFull(self):
        if self.size() >= self.capacity :
            print("Queue is Full")
            return True

    def isEmpty(self):
        if self.size == 0 :
            self.head = -1
            self.tail = -1
            return True

    def enqueue(self, item):
        if self.isFull():
            return
        self.tail += 1
        return  self.items.append(item)

    def dequeue(self):
        if self.isEmpty():

            return None
        self.head +=1
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

#Testing

a = Queue(5)
a.enqueue(3)
a.enqueue(2)
a.enqueue(1)
print(a.items,end="\n")
print(a.size(),end="\n")
a.dequeue()
print(a.items,end="\n")
for i in range(1,6):
    a.enqueue(i)
print(a.items,end="\n")
for j in range(6):
    a.dequeue()
    print(a.items)
print(a.head)

