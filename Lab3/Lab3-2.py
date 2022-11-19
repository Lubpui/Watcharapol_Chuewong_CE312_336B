MainStack = []
StayStack = []
MainStack.append("A")
MainStack.append("B")
MainStack.append("C")
MainStack.append("D")
MainStack.append("E")
MainStack.append("F")

print("Stack Before Reverse")
print("Index    |    Stack  |")
for i in range(len(MainStack)-1,-1,-1):
    print(f"    {i}     "," | ", f"      {MainStack[i]}    "," | ")

for i in range(0,len(MainStack),1):
    StayStack.append(MainStack.pop())
MainStack.extend(StayStack)

print("\nStack After Reverse")
print("Index    |    Stack  |")
for i in range(len(MainStack)-1,-1,-1):
    print(f"    {i}     "," | ", f"      {MainStack[i]}    "," | ")

