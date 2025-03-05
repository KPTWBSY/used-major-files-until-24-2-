class Node:
    def __init__(self,value):
        self.data=value
class Graph:
    def __init__(self):
        self.graph={}
        self.v_list={}
        self.edge=[]
        self.total=0

    def create(self,v,data,weight): #인접리스트 추가
        node=Node(data)
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[v].append((node,weight))

    def sort(self,item):
        temp=[]
        for v1,v2,cost in network:
            if (v1==item or v2==item) and (v1,v2,cost) not in self.edge:
                temp.append((cost,v1,v2))
            temp.sort()
        return (temp[0][0],temp[0][1],temp[0][2])

    def find(self,v2): #원소가 속한 집합 찾기(두 원소가 속한 집합 같으면 사이클 형성?)
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

        while True: #종료조건 추가: n-1개의 간선이 추가되면..
            x=self.sort(start)

            s1=self.find(x[1])
            s2=self.find(x[2])
            print('v1 set: ',s1,',','v2 set: ',s2)
            if s1==s2:
                print("the same set. rejected for cycle")
            self.edge.append((x[1],x[2],x[0]))
            self.total+=x[0]
            self.union(s1,s2)
            print(self.v_list)

            if # 해당 노드에서 더 찾을
                start=x[2]
            else:
                start=x[1]
            print(start)

            #스타트를 하나만 지정하면 안되고 방문한 모든 정점에서 start 할수 있도록 해야함.




            
            

        

g=Graph()
network=[(1,5,6),(1,6,8),(2,3,17),(2,6,9),(5,6,7),(3,7,15),(3,4,5),(3,8,3),(4,8,4),(6,7,10)]

for v,node,weight in network:
    g.create(v,node,weight)
print('network=',network)
g.prim()
print()
