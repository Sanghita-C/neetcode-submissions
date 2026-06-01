class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            size = len(word)
            size = str(size)
            result += size
            result += "#"
            result += word

        return result


    def decode(self, s: str) -> List[str]:
        print("string is : ",s)
        if s in "":
            return []
        i =0 
        word = ""
        size = 0
        parse_word = False
        answer = []

        for char in s :
            print(char,parse_word)

            if parse_word == False:
                if char != "#":
                    word += char
                else:
                    size = int(word)
                    parse_word = True
                    word = ""
                    if size == 0:
                        answer.append("")
                        parse_word = False

            else: 
                if size > 0:
                    word += char
                    size -= 1
                if size == 0:
                    answer.append(word)
                    size = 0
                    parse_word = False
                    word = ""
        if len(answer) ==0 : 
            return [""]

        return answer






