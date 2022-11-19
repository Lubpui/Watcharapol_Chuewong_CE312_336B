class node:
    def __init__(self,val):
        self.prv = None
        self.val = val
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def push(self,val):
        newNode = node(val)
        if self.head == None:
            self.head = newNode
        else:
            poin = self.head
            while poin.next is not None:
                poin = poin.next
            poin.next = newNode
            newNode.prv = poin

    def pushStart(self,val):
        newNode = node(val)
        poin = self.head

        if self.head == None:
            self.head = newNode
        else:
            newNode.next = poin
            self.head = newNode
            poin.prv = newNode

    def delete(self,val):
        poin = self.head

        while poin.val != val:
            if poin.next == None:
                break
            else:
                poin = poin.next
        if poin.next == None and poin.val != val:
            print("This option is not available")
        else:
            print("Delete number '",poin.val,"' complete")

            prevNode = poin.prv
            prevNode.next = poin.next

            prevNode.next.prv = None
            poin.next = None
            poin.prv = None


    def display(self):
        displayVal = self.head
        print("header -> ", end="")
        while displayVal is not None:
            print(displayVal.val, end="")
            displayVal = displayVal.next
            if displayVal is not None:
                print(" -> ", end="")
            else:
                print("")

if __name__ == "__main__":
    List = linkedList()

    List.push(44)
    List.push(36)
    List.push(90)
    List.push(10)
    List.push(60)
    List.push(99)

    while True:
        print("\n-----------------------",
              "\n1 for Insert",
              "\n2 for Insert from header",
              "\n3 for Delete",
              "\n4 for Display",
              "\n5 for exit",
              "\n-----------------------")
        num = int(input("select : "))
        if num == 1:
            inPush = input("Enter the number you want to Insert : ")
            List.push(inPush)
        elif num == 2:
            inPushHead = input("Enter the number you want to Insert : ")
            List.pushStart(inPushHead)
        elif num == 3:
            inDelete = int(input("Enter the number you want to Delete : "))
            List.delete(inDelete)
        elif num == 4:
            List.display()
        elif num == 5:
            break
        else:
            print("This option is not available")
