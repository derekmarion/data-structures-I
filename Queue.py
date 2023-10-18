####API####
# enqueue - add item to beginning
# dequeue - remove and return item from end
# peek - return last item
# size - return number of items
# is_empty - True if no items, False otherwise

class Queue:
    def __init__(self) -> None:
        self.base = []
    
    def enqueue(self, value):
        self.base.insert(0, value)

    def dequeue(self):
        dequeued = self.base.pop(-1)
        print(f"{dequeued} dequeued from the stack")
        return dequeued

    def peek(self):
        peeked = self.base[-1]
        print(f"{peeked} is at the end of the queue")
        return peeked

    def size(self):
        print(f"The queue has {len(self.base)} items")
        return len(self.base)

    def is_empty(self):
        if len(self.base) == 0:
            print("True")
            return True
        print("False")
        return False
    
queue = Queue()


queue.enqueue(1)

queue.enqueue(2)

queue.enqueue(3)

queue.peek()

queue.dequeue()

queue.peek()

queue.size()

queue.is_empty()