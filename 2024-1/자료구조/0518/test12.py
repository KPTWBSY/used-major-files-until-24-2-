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

    def setFW(self):

        self.dist=[]
        self.prev=[]

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

    def FW(self,max):            
            for k in range (max):
                '''k: 0부터 시작해서 len(self.graph)-1 까지. max: len(self.graph부터 시작해서 1까지.'''
                for i in range(len(self.graph)):
                    for j in range(len(self.graph)):
                        if self.dist[i][j]>self.dist[i][k]+self.dist[k][j]:
                            self.dist[i][j]=self.dist[i][k]+self.dist[k][j]

                            self.prev[i][j].append(k)
            
            '''print(self.dist)
            print(self.prev)'''
            return self.dist, self.prev
    
    def FW2(self, max):
        self.setFW()
        self.FW(max) 
        return self.dist, self.prev  
    
    def FW3(self,max):
        if max>1:
            if self.FW2(max)!=self.FW2(max-1):
                for x in range(len(self.graph)):
                    for y in range(len(self.graph)):
                        if self.FW2(max)[1][x][y]!=self.FW2(max-1)[1][x][y]:
                if self.FW2(max)[1]:
                    print(self.FW2(max)[1])
                return self.FW3(max-1)
        elif max<=1:
            x=self.setFW()
            if x!=self.FW2(max):
                print("aAa")

                

                        
'''max=3 >> max=2 >> max=1>> k=0, 1 ,2 '''
'''비용행렬 dist: v*v 형태로 생성. 대각행렬은 모두 0이어야 함. v는 self.graph[v]의 그 v(노드의 개수)'''

'''그래프의 모든 요소의 각각의 인접 리스트 탐색>> dest, weight 있으면 비용행렬의 dest 위치에 weight값 넣기.'''

g=ShortestPath()
for start,dest,weight in [(0,1,4),(0,2,11),(1,2,2),(1,0,6),(2,0,3)]:
    g.create(start,dest,weight)

g.FW3(len(g.graph))

'''어디를 거쳐왔는지에 대한 정보>>p배열
dist가 바뀔때 p배열도 바뀐다
a0에 대한 p배열,1에대한 p배열..각각 만들기
p배열에 아무것도 없다: 경유x.
뭔가 있다>>경유 O
재귀..는..어케쓰지'''