# Part 1: First in last out (FILO)exercise
FILO = []
FILO.append("A")
FILO.append("B")
FILO.append("C")
FILO.append("D")
FILO.append("E")
FILO.append("F")

print("FILO Before Pop")
print("   Index    |      Stack    |")
for i in range(len(FILO)-1,-1,-1):
    print(f"    {i}     "," | ", f"      {FILO[i]}    "," | ")

pop1 = int(input("How many time to pop : "))
BeforePop = len(FILO)
for loopPop1 in range(1, pop1+1, 1):
    if loopPop1 <= BeforePop:
        print(loopPop1,"| Pop : ",FILO.pop())
    else:
        print("|  Stack Underflow  |")
        break
print("\nFILO After Pop")
print("Index    |    Stack  | ")
for j in range(len(FILO)-1,-1,-1):
    print(f"    {j}     ", " | ", f"      {FILO[j]}    ", " | ")

