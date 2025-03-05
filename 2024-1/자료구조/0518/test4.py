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

        while temp!=self.head and self.head.data!=0:
            print(temp.data,end=' ')
            temp=temp.rlink
        print("]",end=' ')

        if not self.empty():
            print("H=%d R=%d I=%d"%(self.head.llink.data,self.head.rlink.data,self.head.data))
        else:
            print("empty")


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
                while tempp.parent.data<tempp.data:
                    a=tempp.parent.data
                    tempp.parent.data=tempp.data
                    tempp.data=a
                tempp=tempp.llink
                child+=1
         	            
    def delete(self):
        if self.empty():
            print("List empty")
            return
        

        self.head.llink.data=self.head.rlink.data
        self.head.rlink.rlink=None
        self.head.rlink=self.head.rlink.llink
        self.head.rlink.rlink.llink=None
        self.head.rlink.rlink=self.head
        self.head.data-=1

        child=2
        tempp=self.head.rlink
        while child<=self.head.data:
            while tempp.parent.data<tempp.data:
                a=tempp.parent.data
                tempp.parent.data=tempp.data
                tempp.data=a
            tempp=tempp.llink
            child+=1
            
        self.view()
        
    def postorder(self):
        postorderlst=[]
        if (self.head.data%2==0):
            x=self.head.rlink       
        elif (self.head.data%2==1):
            x=self.head.rlink.llink

        '''postorderlst.append(x.data)
        postorderlst.append(x.parent.data)

        temp=self.head.rlink
        num=2
        while num<=self.head.data:
            if temp.parent==x.parent and temp.data not in postorderlst:
                postorderlst.append(temp.data)
                temp=temp.parent
            num+=1
            temp=temp.llink

        while True:
            if temp.parent==x.parent and temp.data not in postorderlst;
                postorderlst.append(temp.data)
                x=temp.parent

        for x in postorderlst:
            print(x)'''
        
        '''while x.parent!=None:
            if x.data not in postorderlst: postorderlst.append(x.data)
            if x.parent.data not in postorderlst:postorderlst.append(x.parent.data)

            temp=self.head.rlink
            num=2
            while num<=self.head.data:
                if temp.parent==x.parent and temp.data not in postorderlst:
                    postorderlst.append(temp.data)
                    x=temp.parent
                    break
                num+=1
                temp=temp.llink  

        for x in postorderlst:
            print(x)'''
        

        if x.data not in postorderlst: postorderlst.append(x.data)
        while x.parent!=None:
            x=x.parent
            if x.data not in postorderlst:postorderlst.append(x.data)

            temp=self.head.rlink
            num=2
            while num<=self.head.data:
                if temp.parent==x and temp.data not in postorderlst:
                    postorderlst.append(temp.data)
                    break
                num+=1
                temp=temp.llink  

        for x in postorderlst:
            print(x)
        


lst=LinkedList()
for item in [10,20,5,12,40,80]:
    print('Add',item,end=' ')
    lst.add(item)
    lst.view()

lst.postorder()