class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_frequency = Counter(nums)
        print(count_frequency)

        sorted_frequency = sorted(count_frequency.items(), key = lambda item : item[1], reverse = True)



        print(sorted_frequency)
        answer = []

        for keys in sorted_frequency:
            if k ==0:
                break
            answer.append(keys[0])
            k -=1



        return answer