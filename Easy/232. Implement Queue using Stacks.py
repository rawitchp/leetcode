class MyQueue(object):

    def __init__(self):
        self.arr = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.arr.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        f = self.arr[0]
        self.arr = self.arr[1:]
        return f
        

    def peek(self):
        """
        :rtype: int
        """
        return self.arr[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.arr) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()