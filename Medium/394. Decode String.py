class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for _,char in enumerate(s):
            if char == ']':
                word = ""
                while stack:
                    str = stack.pop()
                    if str == '[':
                        break
                    word = str + word
                times = ""
                while stack:
                    str = stack.pop()
                    if str.isdigit():
                        times = str + times
                    else:
                        stack.append(str)
                        break
                print(times)
                word = word * int(times)
                stack.append(word)
            else:
                stack.append(char)
        return "".join(stack)