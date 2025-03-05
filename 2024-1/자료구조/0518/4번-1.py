class Node:
    def __init__ (self,value):
        self.data=value

class Graph:
    def __init__(self):
        self.graph={}
        self.queue=[]
        self.indegree={}

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
        for x in self.queue:
            print(x, end=' ')
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
                self.showq()

        while self.queue:
            vertex=self.deleteq()
            self.showq()
            print()

            for key in self.graph:
                if vertex in [node.data for node in self.graph[key]]:
                    self.indegree[key]-=1
                    if self.indegree[key]==0:
                        self.addq(key)
                        self.showq()
                        print()
                        self.showIndegree()
                        print()
                    

        self.showIndegree()
            

g=Graph()
for v,node in [(0,2),(1,2),(2,4),(4,6),(6,9),(4,7),(7,10),(3,5),(5,4),(5,8)]:
    g.create(v,node)
g.show()
g.showIndegree()
g.topologicalSort()