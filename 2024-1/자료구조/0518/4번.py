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
            print(x)

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

        
        vertex=self.deleteq()
        for key in self.graph:
            if vertex in [node.data for node in self.graph[key]]:
                self.indegree[key]-=1
                if self.indegree[key]==0:
                    self.addq(key)
    
          
        self.showIndegree()
            

g=Graph()
for v,node in [(1,2),(1,4),(2,3),(3,5),(3,4),(4,3),(4,2),(4,5),(5,2)]:
    g.create(v,node)
g.show()
g.showIndegree()
g.topologicalSort()