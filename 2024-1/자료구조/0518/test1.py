class Node:
    def __init__(self,item):
        self.data=item
        self.rlink=None
        self.llink=None

class LinkedList:
    def __init__(self):
        self.head=Node(0)
        self.head.rlink=self.head
        self.head.llink=self.head

    def empty(self):
        return self.head.rlink==self.head

    def find(self, item):
        temp=self.head.rlink
        while temp!=self.head:
            if temp.data==item: return temp
            temp=temp.rlink
        return None

    def view(self):
        temp=self.head.rlink
        print("[",end=' ')
        while temp!=self.head:
            print(temp.data,end='')
            temp=temp.rlink
        print("]",end=' ')
        if not self.empty():
            print("H=%d R=%d I=%d"%(self.head.rlink.data,self.head.llink.data,self.head.data))
        else:print("List is empty")

    def add(self,item):
        node=Node(item)
        self.head.data+=1
        if self.empty():
            node.llink=self.head
            node.rlink=self.head
            self.head.rlink=node
            self.head.llink=node
        else:
            node.llink=self.head.llink
            node.rlink=self.head
            self.head.llink.rlink=node
            self.head.llink=node

    def delete(self,item):
        if self.empty():
            print("List empty")
            return
        
        node= self.find(item)

        if not node:
            print("Not found")
        if node==self.head:
            print("head is not deleted")
            return
        self.head.data-=1
        node.llink.rlink=node.rlink
        node.rlink.llink=node.llink
        del node

lst=LinkedList()
for item in [100,200,300]:
    print('Add',item,end=' ')
    lst.add(item)
    lst.view()

