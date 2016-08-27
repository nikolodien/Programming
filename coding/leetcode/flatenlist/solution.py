# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from types import *
import itertools

class NestedInteger(object):
    object = None
    def __init__(self,object):
        self.object = object
    def isInteger(self):
        if type(self.object) is IntType:
            return True
        else:
            return False

    def getInteger(self):
        return int(self.object)

    def getList(self):
        return list(self.object)

class NestedIterator(object):
    nestedInteger = None
    stack = []
    def __init__(self, nestedList):
        if nestedList.isInteger():
            self.nestedInteger = nestedList
        else:
            self.nestedInteger = iter(nestedList.getList())

    def next(self):
        val = None
        while(val==None and not self.nestedInteger==None):
            if not type(self.nestedInteger) is IntType:
                try:
                    val = self.nestedInteger.next()
                except StopIteration as si:
                    if(len(self.stack)>0):
                        self.nestedInteger = self.stack.pop()
                    else:
                        break
            if not val.isInteger():
                self.stack.append(self.nestedInteger)
                self.nestedInteger = iter(val.getList())
                val = None
            else:
                val = val.getInteger()
        return val
    
    def hasNext(self):
        val, peek = False, None
        while(not self.nestedInteger==None):
            if not type(self.nestedInteger) is IntType:
                try:
                    peek = self.nestedInteger.next()
                    if not peek==None:
                        if peek.isInteger():
                            print peek.getInteger()
                        val = True
                        break
                    self.nestedInteger = itertools.chain([peek],self.nestedInteger)
                except StopIteration as si:
                    if len(self.stack)>0:
                        self.nestedInteger = self.stack.pop()
                    else:
                        break
        return val

# Your NestedIterator object will be instantiated and called as such:
nestedList = NestedInteger([NestedInteger(1),NestedInteger(2),NestedInteger([NestedInteger(1),NestedInteger(2)])])
i, v = NestedIterator(nestedList), []
if(i.hasNext()):
    v.append(i.next())
if(i.hasNext()):
    v.append(i.next())
if(i.hasNext()):
    v.append(i.next())
if(i.hasNext()):
    v.append(i.next())            
print v