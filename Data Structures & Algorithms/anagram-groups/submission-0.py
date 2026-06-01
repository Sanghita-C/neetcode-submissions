class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        num_strs = len(strs)
        char_count_map = {}
        answer = []

        for word in strs:
            char_count_list = [0]*26
            for char in word:
                char_count_list[ord(char) - ord('a')] +=1

            counter_tupple = tuple(char_count_list)

            if counter_tupple in char_count_map.keys():
                char_count_map[counter_tupple].append(word)
            else:
              char_count_map[counter_tupple] = [word]



            

        for key in char_count_map.keys():
            answer.append(char_count_map[key])
        
        return answer



        