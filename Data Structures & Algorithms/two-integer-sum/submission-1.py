
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sample = {}
        for i, num in enumerate(nums):
            inverse = target - num
            if inverse in sample:
                return [sample[inverse],i]
            sample[num]=i
        