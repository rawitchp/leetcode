class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = ''
        for i in range(len(s)):
            print(string)
            if(len(string) == 0):
                string += s[i]
            elif(string[-1] == '(' and s[i] == ')'):
                string = string[:len(string)-1]
            elif(string[-1] == '[' and s[i] == ']'):
                string = string[:len(string)-1]
            elif(string[-1] == '{' and s[i] == '}'):
                string = string[:len(string)-1]
            else:
                if(s[i] == ')' or s[i] == '}' or s[i] == ']'):
                    return False
                string += s[i]
        if(len(string) == 0):
            return True
        return False

            
            
        