class Node:
    def __init__(self,item):
        self.data=item
        self.parent=None
        self.rlink=None
        self.llink=None

class LinkedList:
    def __init__(self):
        self.head=Node(0)
        self.head.parent=None
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
        temp=self.head.llink
        print("[",end=' ')
        while temp!=self.head:
            print(temp.data,end=' ')
            temp=temp.rlink
        print("]",end=' ')
        if not self.empty():
            print("H=%d R=%d I=%d"%(self.head.llink.data,self.head.rlink.data,self.head.data))
        else:print("List is empty")


    def add(self,item):

        node=Node(item)
        self.head.data+=1
        x=self.head.data

        if self.empty():
            node.llink=self.head
            node.rlink=self.head
            self.head.rlink=node
            self.head.llink=node

        else:
            node.llink=self.head.rlink            
            node.rlink=self.head            
            self.head.rlink.rlink=node
            self.head.rlink=node
            
            temp=self.head.llink
            y=1
            while y<x//2:
                temp=temp.rlink
                y+=1
            node.parent=temp

            child=2
            tempp=self.head.rlink
            while child<=self.head.data:
                '''여기다 while문 넣어야 하나?'''

                '''if tempp.parent.data<tempp.data:
                    a=tempp.parent.data
                    tempp.parent.data=tempp.data
                    tempp.data=a
                tempp=tempp.rlink'''

                while tempp.parent.data<tempp.data:
                    a=tempp.parent.data
                    tempp.parent.data=tempp.data
                    tempp.data=a
                tempp=tempp.llink
                child+=1

         	            
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

    def isEmpty(self):
        return self.head.data==0

lst=LinkedList()
for item in [10,20,5,12,40,80]:
    print('Add',item,end=' ')
    lst.add(item)
    lst.view()