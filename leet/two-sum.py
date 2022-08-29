class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        index = 0
        for num in nums:
            # total to look for based on the current num
            tmp_total = target - num
            # if tmp target exists, return
            if mapping.get(tmp_total) != None:
                return [mapping.get(tmp_total), index]
            
            mapping[num] = index
            index += 1