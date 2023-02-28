class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CreateList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next  = self.head
    #adding node at the end of LL
    def add(self,data):
        newNode = Node(data)
    #Is empty?
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
            #It is CLl,so tail will point to head
            self.tail.next = self.head

    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        else:
            print("Nodes of the linked list:")
            print(current.data,"-->")
            while (current.next != self.head):
                current = current.next
                print(current.data,"-->")

class CircularLinkedList:
    c1 = CreateList()
    c1.add("S")
    c1.add("M")
    c1.add("I")
    c1.add("L")
    c1.add("E")
    c1.display()
