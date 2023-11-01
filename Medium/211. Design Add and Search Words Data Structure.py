class WordDictionary:

    def __init__(self):
        self.dict = {}
        

    def addWord(self, word: str) -> None:
        a = self.dict
        for i in word:
            if not i in a:
                a[i] = {}
            a = a[i]
        a['#'] = {}
        

    def search(self, word: str) -> bool:
        def deep_search(word,dic):
            a = dic
            if word == "":
                if '#' in a:
                    return True
                else:
                    return False
            if word[0] == '.':
                for i in a:
                    if deep_search(word[1:],a[i]):
                        return True
            elif word[0] in a:
                if deep_search(word[1:],dic[word[0]]):
                    return True   
            return False
        return deep_search(word,self.dict)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)