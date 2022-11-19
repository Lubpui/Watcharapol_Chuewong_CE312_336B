# Part 2: First in firstout (FIFO)exercise
FIFO = []
FIFO.append("A")
FIFO.append("B")
FIFO.append("C")
FIFO.append("D")
FIFO.append("E")
FIFO.append("F")

print("FIFO Before Pop")
print("Index    |    Stack  |")
for i in range(len(FIFO)-1,-1,-1):
    print(f"    {i}     "," | ", f"      {FIFO[i]}    "," | ")

pop1 = int(input("How many time to pop : "))
BeforePop = len(FIFO)
for loopPop1 in range(1, pop1+1, 1):
    if loopPop1 <= BeforePop:
        print(loopPop1,"| Pop : ",FIFO.pop(0))
    else:
        print("|  Stack Underflow  |")
        break
print("\nFIFO After Pop")
print("Index    |    Stack  | ")
for j in range(len(FIFO)-1,-1,-1):
    print(f"    {j}     ", " | ", f"      {FIFO[j]}    ", " | ")


