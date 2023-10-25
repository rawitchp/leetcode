class Trie(object):

    def __init__(self):
        self.root = {}
      
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['end'] = {}

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return 'end' in node
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)