####API####
# push - add item to top
# pop - remove and return item from top
# peek - return top item
# size - return number of items
# is_empty - True if no items, False otherwise


class Stack:
    def __init__(self) -> None:
        self.base = []
    
    def push(self, value):
        self.base.insert(0, value)

    def pop(self):
        popped = self.base.pop(0)
        print(f"{popped} popped from the stack")
        return popped

    def peek(self):
        peeked = self.base[0]
        print(f"{peeked} is at the top of the stack")
        return peeked

    def size(self):
        print(f"The stack has {len(self.base)} items")
        return len(self.base)

    def is_empty(self):
        if len(self.base) == 0:
            print("True")
            return True
        print("False")
        return False

stack = Stack()

stack.push(19)

stack.push(3)

stack.push(8)

stack.peek()

stack.size()

stack.is_empty()

stack.pop()

stack.peek()