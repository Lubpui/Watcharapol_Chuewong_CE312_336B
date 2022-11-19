class graph:
    def __init__(self, val = None):
        self.list = [[' ']]

    def insert(self, val = None):
        self.list[0].append(val)
        self.list.append([val])

        l = len(self.list)-1

        while l > 0:
            if len(self.list[0]) != len(self.list[l]):
                self.list[l].append("0")
            elif len(self.list[0]) == len(self.list[l]):
                l -= 1

    def connect(self,nodeA,nodeB):
        for j in self.list[1:len(self.list)]:
            if nodeA in j:
                pointA = self.list.index(j)
        for i in self.list[0]:
            if i is nodeB:
                pointB = self.list[0].index(i)

        self.list[pointA][pointB] = '1'
        self.list[pointB][pointA] = '1'

    def disconnect(self,nodeA,nodeB):
        for j in self.list[1:len(self.list)]:
            if nodeA in j:
                pointA = self.list.index(j)
        for i in self.list[0]:
            if i is nodeB:
                pointB = self.list[0].index(i)

        self.list[pointA][pointB] = '0'
        self.list[pointB][pointA] = '0'


    def display_Matrix(self):
        for i in self.list:
            for j in i:
                print(j,end="  ")
            print("\n")

    def display_List(self):
        for i in range(1,len(self.list)):
            print(self.list[i][0],"| ",end="")
            for j in range(len(self.list[i])):
                if self.list[i][j] == '1':
                    print(self.list[0][j],end="")
            print("\n")

    def display_EdgeList(self):
        edgeList = []
        x = 0
        for i in range(1,len(self.list)):
            for j in range(len(self.list[i])):
                val = [self.list[i][0],self.list[0][j]]
                val.sort()
                if self.list[i][j] == '1' and val not in edgeList:
                    edgeList.append(val)
                    print(f"Edge List {[x]}: ",end="")
                    for z in edgeList[x]:
                        print(z,end="")
                    x += 1
                    print("\n")

g = graph()

#Create Graph
g.insert('A')
g.insert('B')
g.insert('C')
g.insert('D')
g.insert('E')
g.insert('F')

#Connect Node
g.connect('A','B')
g.connect('A','C')
g.connect('C','D')
g.connect('C','F')
g.connect('E','F')

g.disconnect('C','F')
g.disconnect('A','B')
g.disconnect('C','D')

g.connect('A','E')
g.connect('B','C')
g.connect('D','F')

print("-"*20,"\nAdjacency matrix\n","-"*20)
g.display_Matrix()
print("-"*20,"\nAdjacency list\n","-"*20)
g.display_List()
print("-"*20,"\nEdge list\n","-"*20)
g.display_EdgeList()




