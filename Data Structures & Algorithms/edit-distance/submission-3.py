class Solution:
    def __init__(self):
        self.memo = {}
    def minDistance(self, word1: str, word2: str) -> int:
        """
        monkeys money
        onkeys oney
        nkeys  ney
        keys   ey --- remove k + (eys , ey)
                  --- insert e + (ekeys, ey)
                  --- change k -e + (eeys,ey)


        Base condition: 

        if first character of string same 
        count += (downward calls)

        if first character doesn't match:
            if one of them is "" then count = length of other string
            if both of them are "" return 0 
            count += 1+ min( count(all possible downward options))



        """
        if (word1,word2) in self.memo:
            return self.memo[(word1,word2)]
        if word1 == "" and word2 == "":
            return 0
        if word1 =="" or word2 =="":
            return max(len(word1), len(word2))
        
        if word1[0] == word2[0]:
            self.memo[(word1, word2)] = self.minDistance(word1[1:],word2[1:])
            return self.memo[(word1, word2)]
        else:
            self.memo[(word1, word2)] = 1 + min(self.minDistance(word1[1:], word2), self.minDistance(word2[0]+word1, word2), self.minDistance(word2[0]+word1[1:], word2))
            return self.memo[(word1, word2)]
        
        return 0