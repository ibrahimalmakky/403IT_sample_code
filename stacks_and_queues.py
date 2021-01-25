class DataStructure:

    def __init__(self):
        self.items = []

    def len(self):
        return len(self.items)

class Stack(DataStructure):

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

# Create a class that implements a queue, with the functions to enqueue and dequeue
class Queue(DataStructure):

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0)

my_stack = Stack()
[my_stack.push(x) for x in range(0, 15) if x%2 == 0]
print(my_stack.pop())

my_queue = Queue()
[my_queue.enqueue(x) for x in range(1, 15) if x%2 == 0]
print(my_queue.dequeue())
