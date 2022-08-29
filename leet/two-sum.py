class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, num in enumerate(nums):
            # total to look for based on the current num
            tmp_total = target - num
            # if tmp target exists, return
            if mapping.get(tmp_total) != None:
                return [mapping.get(tmp_total), i]
            
            mapping[num] = i     