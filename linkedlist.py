class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        i = 0
        while current and i < index:
            prev = current
            current = current.next
            i += 1
        if current:
            prev.next = current.next
        else:
            print("Index out of range")

    def update(self, index, data):
        if index == 1:
            self.head.data = data
        else:
            curr = self.head
            i = 0
            while curr and i < index:
                curr = curr.next
                i += 1
            if curr:
                curr.data = data
            else:
                print("No value existing to be updated!")
    
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end = "->")
            curr = curr.next
        print("None")

if __name__ == "__main__":
    linked = LinkedList()
    linked.insert(1)
    linked.insert(2)
    linked.insert(3)
    linked.insert(4)
    linked.insert(5)
    linked.insert(6)
    linked.update(0, 7)
    linked.remove(0)
    linked.display()