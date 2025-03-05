class Node:
    def __init__ (self,value):
        self.data=value

class Graph:
    def __init__(self):
        self.graph={}
        self.queue=[]
        self.indegree={}
        self.route=[]

    def create(self,data,v):
        node=Node(data)
        if v not in self.graph:
            self.graph[v]=[]
        if data not in self.graph:
            self.graph[data]=[]
        self.graph[v].append(node)


    def setIndegree(self):
        for x in self.graph:
            self.indegree[x]=len(self.graph[x])

    
    def show(self):
             sorted_dic=sorted(self.graph.items())
             for no, alist in sorted_dic:
                print("[" , no ,"]", end=' ')
                for node in alist:
                    print(node.data,end=' ')
                print()

    def addq(self,v): self.queue.append(v)

    def deleteq(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            print("Queue Empty")
    
    def showq(self):
        print('[', end=' ')
        for x in self.queue:
            print(x, end=' ')
        print(']')
        print()

    def showIndegree(self):
        shorted_indegree=sorted(self.indegree.items())
        for key,value in shorted_indegree:
            print(key,':',value)
    
    def topologicalSort(self):
        self.setIndegree()
        for x in self.indegree:
            if self.indegree[x]==0:
                self.addq(x)
                print("큐에 ",x,"추가" )
                
        self.showq()

        while self.queue:
            vertex=self.deleteq()
            print("큐에서 ", vertex, "제거")
            self.route.append(vertex)
            
            a=len(self.queue)
            print()
            self.showIndegree()
            self.showq()


            for key in self.graph:
                if vertex in [node.data for node in self.graph[key]]:
                    self.indegree[key]-=1
                    if self.indegree[key]==0:
                        self.addq(key)
                        print("큐에 ",key,"추가" )
            b=len(self.queue)

            if a!=b:
             print()
             self.showIndegree()
             self.showq()
        print("모든 정점 방문, 위상정렬 종료.")
        print("위상 정렬 순서: ", end=' ')
        for x in self.route:
            print(x, end=' ')

g=Graph()
for v,node in [(0,1),(0,2),(1,3),(1,4),(2,4),(4,3),(3,5),(3,6),(4,6),(5,7),(6,7),(4,7)]:
    g.create(v,node)
g.show()
g.showIndegree()
g.topologicalSort()