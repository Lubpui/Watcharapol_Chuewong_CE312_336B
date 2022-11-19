class node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def push(self,val):
        newNode = node(val)
        if self.head == None:
            self.head = newNode
        else:
            listed = self.head
            while listed.next != None:
                listed = listed.next
            listed.next = newNode
            newNode.prev = listed

    def display(self):
        displayVal = self.head
        while displayVal != None:
            print(displayVal.val,end="")
            if displayVal.next != None:
                print(" <-> ",end="")
            else:
                print(end="")
            displayVal = displayVal.next

List = linkedList()

List.push(1)
List.push(2)
List.push(3)
List.push(4)

List.display()

