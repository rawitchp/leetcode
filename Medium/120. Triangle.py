# class Solution(object):
#     def minimumTotal(self, triangle):
#         """
#         :type triangle: List[List[int]]
#         :rtype: int
#         """
#         dic = {}
#         def call(row,i):
#             l = 0
#             r = 0
#             if(row == len(triangle)):
#                 return 0
           
#             if(dic.has_key(row+1) and dic[row+1].has_key(i)):
#                 l = dic[row+1][i]
#             else:
#                 l = call(row+1,i)
#                 if(dic.has_key(row+1)):
#                     dic[row+1][i] = l
#                 else:
#                     dic[row+1] = {}
#                     dic[row+1][i] = l
#             if(dic.has_key(row+1) and dic[row+1].has_key(i+1)):
#                 r = dic[row+1][i+1]
#             else:
#                 r = call(row+1,i+1)
#                 if(dic.has_key(row+1)):
#                     dic[row+1][i+1] = r
#                 else:
#                     dic[row+1] = {}
#                     dic[row+1][i+1] = r
#             return triangle[row][i] + min(l,r)
#         return call(0,0)
        
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for depth in range(len(triangle)-2,-1,-1):
            for i in range(depth+1):
                triangle[depth][i] += min(triangle[depth+1][i],triangle[depth+1][i+1])
        return (triangle[0][0])
        