# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.cursor = -1
        self.flat_arr = self.flat(nestedList)
    
    def next(self) -> int:
        self.cursor += 1
        return self.flat_arr[self.cursor]
    
    def hasNext(self) -> bool:
        return self.cursor < len(self.flat_arr) -1

    def flat(self, arr) -> None:
        temp = []
        for item in arr:
            if item.isInteger():
                temp.append(item.getInteger())
            else:
                temp += (self.flat(item.getList()))
        return temp


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())