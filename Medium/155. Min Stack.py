class MinStack(object):

    def __init__(self):
        self.root = []
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.root.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        else:
            if self.min[-1] >= val:
                self.min.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        pop = self.root.pop()
        if pop == self.min[-1]:
            self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.root[len(self.root)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()