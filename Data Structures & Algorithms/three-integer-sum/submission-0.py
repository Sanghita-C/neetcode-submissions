class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        [x1 ,x2,x3,x4,x5 ,x6, x7,x8].      {
                                                num : index
                                            }

        (x2,x5,x6), (x1,x4,x5)

        loop i:                     loop i : 
            loop j:                     target = (- nums[i]), put this in hashmap
                                         loop j :
                loop k: `                  check hashmap for target - num[j] - if exists : put nums[i], num[j],                                                                     target-num[j] in the list


        """

        answer = [] 
        nums = sorted(nums)
        print(f"sorted array = {nums}")

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l= i+1
            r = len(nums)-1
            #print(f"a = {nums[i]}")

            while l<r:
                #print(f"potential candidates {nums[i]}, {nums[l]} and {nums[r]} sum upto {nums[i] + nums[l] + nums[r]}")
                if nums[l] + nums[r] > (-nums[i]):
                    r -=1
                elif nums[l] + nums[r] < (-nums[i]):
                    l +=1
                
                else: 
                    answer.append([nums[i],nums[l],nums[r]])
                    j = l+1
                    while j < r and nums[j] == nums[l]:
                        j+=1
                    l=j
            
        return answer

                

        