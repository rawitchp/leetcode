class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op = {"+":"+","-":"-","*":"*","/":"/"}
        print(op)
        stack = []
        for i in tokens:
            if not op.has_key(i):
                stack.append(i)
                continue
            b = float(stack.pop())
            a = float(stack.pop())
            ans = 0
            if i == "+":
                ans = a + b
            elif i == "-":
                ans = a - b
            elif i == "*":
                ans = a * b
            elif i == "/":
                ans = a / b
                string = str(ans).split('.')
                if ans < 0 and int(string[1][0]) < 5 :
                     ans = round(ans)
                else:
                    ans = int(ans)  
            stack.append(ans)     
        return int(stack[0])