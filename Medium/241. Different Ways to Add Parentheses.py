class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def checkOp(ch):
            return ch == '*' or ch == '+' or ch == '-'

        def recursion(str):
            res = []
            for i in range(len(str)):
                if checkOp(str[i]):
                    l = recursion(str[:i])
                    r = recursion(str[i+1:])
                    for j in l:
                        for k in r:
                            if str[i] == '+':
                                res.append(int(j)+int(k))
                            elif str[i] == '*':
                                res.append(int(j)*int(k))
                            elif str[i] == '-':
                                res.append(int(j)-int(k))
            if len(res) == 0:
                return [int(str)]
            return res
        return recursion(expression)