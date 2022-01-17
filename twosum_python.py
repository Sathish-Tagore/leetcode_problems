class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for ind, val in enumerate(nums):
            if target - val in hash_map:
                return [hash_map[target - val], ind]
            else:
                hash_map[val] = ind
        return
