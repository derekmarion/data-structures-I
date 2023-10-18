####API####
# insert - add node to beginning (or end)
# search - find and return a given node
# remove - remove a given node
# size - return number of nodes
# is_empty - True if no nodes, False otherwise


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        old_node = self.head
        self.head = new_node
        self.head.next = old_node

    def search(self, value):
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

        return "Node not found"

    def remove(self, value):
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_node.value == value:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                return True
            previous_node = current_node
            current_node = current_node.next

        return False

    def size(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def is_empty(self):
        return self.head is None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


list = LinkedList()

list.insert(10)
list.insert(20)
list.insert(30)

print(list.size())

node = list.search(20)
print(node.value)

removed = list.remove(20)
print(removed)

print(list.size())

print(list.is_empty())