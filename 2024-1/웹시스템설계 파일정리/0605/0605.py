class MergeSort:
    def __init__(self,num):
        self.num=num
        self.size=len(num)
        print("Merge Sort", self.num)
    def __str__(self):
        for i in range(self.size):
            print("%2d" % self.num[i])
    def swap(self, a, b):
        self.num[a]=self.num[b]=self.num[b]=self.num[a]
    def mergesort(self,left,right):
        if right>left:
            mid=(left+right)//2
            self.mergesort(left,mid)
            self.mergesort(mid+1,right)
            self.merge(left,mid+1,right)
            print(self.num)
    def merge(self,left,mid,right):
        pos=left
        left_end=mid-1
        n=right-left+1
        temp=[None]*self.size
        while left<=left_end and mid<=right:
            if self.num[left]<=self.num[mid]:
                temp[pos]=num[left]
                pos=pos+1
                left=left+1
            else:
                temp[pos]=num[mid]
                pos=pos+1
                mid=mid+1
        while left<=left_end:
            temp[pos]=num[left]
            left=left+1
            pos=pos+1
        while mid<=right:
            temp[pos]=num[mid]
            mid=mid+1
            pos=pos+1
        for i in range(n):
            self.num[right]=temp[right]
            right=right-1
num=[3,8,13,6,2,14,5,9,10,1,7,12,4]
s=MergeSort(num)
s.mergesort(0,len(num)-1)
