class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        a z x z y a x y z
                s       e

        len = 4
        maxlen = 4
        set {
            a = 5
            z = 3
            x = 2
            y = 4
            
        }

        start=0 ,  end = 1
        dict - char: index

        while end < len:
            is the end char there in dict : yes : 
                - index marked >= start:
                    start = index marked + 1
                    -len manipulation
                    - maxlen = max 
                index marked < start: 
                    update the index marked to latest 
                    len +=1
            if char not in dictionary: 
                - add char to dictionary and index 
                - 
        """

        start = 0
        end = 1

        if len(s) ==0:
            return 0

        if len(s) ==1:
            return 1

        char_map = {}
        char_map[s[start]] = 0
        maxlen = 1
        length = 1

        while end < len(s):
            if s[end] in char_map:
                if char_map[s[end]] >= start:
                    start = char_map[s[end]] + 1
                    char_map[s[end]] = end
                    length = end - start + 1
                    maxlen = max(maxlen, length)

                else:
                    char_map[s[end]] = end
                    length +=1
                    maxlen = max(maxlen, length)


            else:
                length +=1
                maxlen = max(maxlen, length)
                char_map[s[end]] = end
            end+=1

        return maxlen 
                
                

        
        