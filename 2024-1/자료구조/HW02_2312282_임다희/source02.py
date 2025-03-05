class Node:
    def __init__(self,value):
        self.data=value
class Graph:
    def __init__(self):
        self.graph={}
        self.v_list={}
        self.edge=[]
        self.visitedList=[]
        self.total=0

    def create(self,v,data,weight): #인접리스트 추가
        node=Node(data)
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[v].append((node,weight))

    def sort(self,item_list):
        temp=[]
        for item in item_list:
            for v1,v2,cost in network:
                if (v1==item or v2==item) and ((v1,v2,cost) not in self.edge and (v1,v2,cost) not in self.visitedList):
                    temp.append((cost,v1,v2))
                temp.sort()
        return (temp[0][0],temp[0][1],temp[0][2])

    def find(self,v2): 
        for v1, lst in self.v_list.items():
            if v2==v1:return v1
            if v2 in self.v_list[v1]:return v1
        return -1

    def union(self,s1,s2):
        if s1<s2:
            self.v_list[s1].append(s2)
            self.v_list[s1].extend(self.v_list[s2])
            del self.v_list[s2]
        else:
            self.v_list[s2].append(s1)
            self.v_list[s2].extend(self.v_list[s1])
            del self.v_list[s1]

    def prim(self):
        for v1,v2,cost in network:
            if v1 not in self.v_list:
                self.v_list[v1]=[]
            if v2 not in self.v_list:
                self.v_list[v2]=[]
        print('set list=',self.v_list)
        
        start=int(input("시작 노드 입력"))
        start_list=[]
        start_list.append(start)
        length=len(self.v_list)

        while True: #종료조건 추가: n-1개의 간선이 추가되면..이거만 추가하면 끝날것같은데..
            if length-1==len(self.edge):
                break
            x=self.sort(start_list)

            s1=self.find(x[1])
            s2=self.find(x[2])
            print('v1 set: ',s1,',','v2 set: ',s2)
            if s1==s2:
                print("the same set. rejected for cycle")

            else:
                self.edge.append((x[1],x[2],x[0]))
                self.total+=x[0]
                self.union(s1,s2)
                print(self.v_list)

                if x[1] not in start_list:
                    start_list.append(x[1])

                if x[2] not in start_list:
                    start_list.append(x[2])
            
            self.visitedList.append((x[1],x[2],x[0]))
        print("verticles:" ,start_list)
        print("edges: ", self.edge)
        print("total:" ,self.total)

g=Graph()
network=[(1,2,5),(1,4,3),(2,5,10),(3,5,8),(3,7,11),(4,5,6),(4,6,7),(5,7,13),(6,7,15)]
for v,node,weight in network:
    g.create(v,node,weight)
print('network=',network)
g.prim()
print()
