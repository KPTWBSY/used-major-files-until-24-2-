class Node:
    def __init__(self,node,weight):
        self.data=node
        self.weight=weight

class ShortestPath:

    def __init__(self):
        self.graph={}
        self.visit=[]
        self.dist=[]
        self.prev=[]


    def create(self,v,dest,weight):
        node=Node(dest,weight)
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[v].append(node)
        if dest not in self.graph:
            self.graph[dest]=[]

    def createpath(self):
        for x in range(len(self.graph)):
            self.visit.append([])
            for y in range(len(self.graph)):
                self.visit[x].append([])

    def printdist(self):
        for x in range(len(self.dist)):
            print(x,":",end=" ")
            for y in range(len(self.dist[x])):
                print(self.dist[x][y],end=" ")
            print()
        print()           

    def Floyd_Warshall(self):

        for x in range(len(self.graph)):
            self.dist.append([])
            for y in range(len(self.graph)):
                self.dist[x].append("inf")

        for x in range(len(self.graph)):
            self.prev.append([])
            for y in range(len(self.graph)):
                self.prev[x].append([])

        for x in range(len(self.graph)):
            for y in range(len(self.graph)):
                if x==y:
                    self.dist[x][y]=0
                
                else:
                    if x in self.graph:
                        for node in self.graph[x]:
                            vertex=node.data
                            cost=node.weight
                            if y==vertex:
                                self.dist[x][y]=cost
        print("dist: A-1")
        self.printdist()

        for k in range(len(self.graph)):
            for i in range(len(self.graph)):
                for j in range(len(self.graph)):
                    if self.dist[i][j]!="inf" and self.dist[i][k]!="inf" and self.dist[k][j]!="inf":
                        if self.dist[i][j]>self.dist[i][k]+self.dist[k][j]:
                            self.dist[i][j]=self.dist[i][k]+self.dist[k][j]
                            self.prev[i][j]=k

                    elif self.dist[i][j]=="inf" and self.dist[i][k]!="inf" and self.dist[k][j]!="inf":
                        self.dist[i][j]=self.dist[i][k]+self.dist[k][j]
                        self.prev[i][j]=k

            print("dist: A",k)
            self.printdist()
               
        for x in range(len(self.graph)):
            for y in range(len(self.graph)):
                self.showFW(x,y)
        
        for x in range(len(self.dist)):
            for y in range(len(self.dist)):
                if x!=y:
                    print("s~d: ", x, y,", path [", x, end=' ')
                    for z in range(len(self.visit[x][y])):
                        print(self.visit[x][y][z], end=' ')
                    print(y,']',end=' ')
                    print("len =",self.dist[x][y])

    def showFW(self,x,y):
        if self.prev[x][y]!=[]:

            a=self.showFW(x,self.prev[x][y])
            b=self.showFW(self.prev[x][y],y)

            if a not in self.visit[x][y] and a!=None:
                self.visit[x][y].append(a)
            
            if self.prev[x][y] not in self.visit[x][y]:
                self.visit[x][y].append(self.prev[x][y])
            
            if b not in self.visit[x][y] and b!=None:
                self.visit[x][y].append(b)

            return self.prev[x][y]        

g=ShortestPath()
for start,dest,weight in [(0,1,8),(0,2,3),(0,3,6),(1,3,1),(1,2,4),(3,0,7),(3,2,2)]:
    g.create(start,dest,weight)
g.createpath()
g.Floyd_Warshall()
