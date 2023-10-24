"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        new={}
        def dfs(node,new):
            if not node:
                return None
            if node in new:
                return new[node]
            copy = Node(node.val)
            new[node] = copy
            for i in node.neighbors:
                copy.neighbors.append(dfs(i,new))
            return copy
        return dfs(node,new)    