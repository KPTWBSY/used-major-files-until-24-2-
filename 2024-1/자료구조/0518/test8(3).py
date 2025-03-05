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
        self.min_list={}

    def create(self,v,dest,weight):
        node=Node(dest,weight)
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[v].append(node)


    def createpath(self):
        for x in range(len(self.graph)):
            self.visit.append([])
            for y in range(len(self.graph)):
                self.visit[x].append([])
        print(self.visit)

    def Floyd_Warshall(self):
            
        '''모든 요소들의 값 infi로 지정해둠. (초기값)'''
        for x in range(len(self.graph)):
            self.dist.append([])
            for y in range(len(self.graph)):
                self.dist[x].append(9999)

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

        for k in range(len(self.graph)):
            for i in range(len(self.graph)):
                for j in range(len(self.graph)):
                    if self.dist[i][j]>self.dist[i][k]+self.dist[k][j]:
                        self.dist[i][j]=self.dist[i][k]+self.dist[k][j]

                        self.prev[i][j]=k

            print(self.dist)
            
        print(self.prev)


                                                          

        '''비용행렬 dist: v*v 형태로 생성. 대각행렬은 모두 0이어야 함. v는 self.graph[v]의 그 v(노드의 개수)'''

        '''그래프의 모든 요소의 각각의 인접 리스트 탐색>> dest, weight 있으면 비용행렬의 dest 위치에 weight값 넣기.'''

g=ShortestPath()

for start,dest,weight in [(0,1,4),(0,2,11),(1,2,2),(1,0,6),(2,0,3)]:
    g.create(start,dest,weight)

g.createpath()
g.Floyd_Warshall()


