class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        traveled = [[0 for col in range(len(image[0]))] for row in range(len(image))]

        def recursion(sr,sc,traveled):
            if(sr > len(traveled)-1  or sr < 0 or sc > len(traveled[0])-1 or sc < 0):
                return traveled
            if(traveled[sr][sc] == 1):
                return traveled
            traveled[sr][sc] = 1
            if(image[sr-1][sc] == image[sr][sc]):
                traveled = recursion(sr-1,sc,traveled)
            if(sr+1 < len(traveled) and image[sr+1][sc] == image[sr][sc]):
                traveled = recursion(sr+1,sc,traveled)
            if(image[sr][sc-1] == image[sr][sc]):
                traveled = recursion(sr,sc-1,traveled)
            if(sc + 1 < len(traveled[0]) and image[sr][sc+1] == image[sr][sc]):
                traveled = recursion(sr,sc+1,traveled)
            image[sr][sc] = color
            return traveled
          
        if(image[sr][sc] != color):
            recursion(sr,sc,traveled)
        return image
            
            
            
        