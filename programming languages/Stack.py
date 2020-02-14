class StackUnderFlow(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
class Stack:
    class Node:
        def __init__(self,data,next):
            self.data = data
            self.next = next
        def getData(self):
            return self.data
        def getNext(self):
            return self.next

    def __init__(self):
        self.top = None
        self.count = 0
    def push(self, item):
        self.top = Stack.Node(item,self.top)
        self.count+=1
    def pop(self):
        try:
            item=self.top.getData()
            self.top=self.top.getNext()
            self.count-=1
        except:
            StackUnderFlow("Underflow")
        return item
    def isEmpty(self):
        return self.top==None
    def size(self):
        return self.count
    def print(self):
        out=""
        n=self.top
        while n!=None:
            out+=str(n.getData())+"\n"
            n=n.getNext()
        return out