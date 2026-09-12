class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset_map = {}

        def subarray_search(arr):
            key = tuple(arr)

            if len(arr) == 0:
                return {()}

            if key in subset_map:
                return subset_map[key]

            final_set = {key}

            for i in range(len(arr)):
                # Remove arr[i]
                combined = arr[:i] + arr[i + 1:]

                combined_set = subarray_search(combined)

                for item in combined_set:
                    final_set.add(item)

            subset_map[key] = final_set
            return final_set

        final_set = subarray_search(nums)

        return [list(item) for item in final_set]