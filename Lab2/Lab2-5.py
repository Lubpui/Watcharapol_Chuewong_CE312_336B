array = [["Number ID","Name","Count","Status"],[]]

print(len(array))

array.insert(1,[1,"Rubber",0,"Out of stock"])
array.insert(2,[2,"Ruler",5,"In stock"])
array.insert(3,[3,"Pencil",1,"In stock"])
array.insert(4,[4,"Pen",10,"In stock"])
array.insert(5,[5,"Colour pencil",5,"In stock"])
array.insert(6,[6,"A4 Paper",0,"Out of stock"])

print(array)

#loop print list only In stock
for x in array:
    for y in x:
        if y == "In stock":
            print(x)

#loop print list only Out of stock
for x in array:
    for y in x:
        if y == "Out of stock":
            print(x)

# buys Item function
def buysItem(array):
    n = 1
    while int(n) >= 1:
        print("\nRemaining item :")
        for remain in range(1,len(array),1):
            print(array[remain])
        item = input("what item do you want (Enter products ID): ")
        if 7 > int(item) > 0:
            how = input("How many pieces : ")
            n = input("Do you want any other products? (1 for Yes/ 0 for No) : ")

            for i in range(0,len(array),1):
                for j in range(0,len(array[i]),1):
                    if str(array[i][0]) == item:
                        array[i][2] = array[i][2]-int(how)
                        if array[i][2] == 0:
                            array[i][3] = "Out of stock"
                            break
                        elif array[i][2] < 0:
                            array[i][2] = 0
                            print(array[i][1]," Out of stock")
                            break
                        else:
                            break
        else:
            print("--Try again--")
            print("This ID doesn't exist on the list.")
            return buysItem(array)

    for ar in array:
        print(ar)
# call function
buysItem(array)

