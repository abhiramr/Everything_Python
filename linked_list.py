#import sys

class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next = None

    def getData(self):
        return self.data

    def setData(self,newData):
        self.data=newData

    def setNext(self,newnext):
        self.next=newnext
