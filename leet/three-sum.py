class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            left_ptr = i +1 
            right_ptr = len(nums) -1
            
            while left_ptr < right_ptr:
                    
                left_val = nums[left_ptr]
                right_val = nums[right_ptr]
                tmp_sum = left_val + right_val + num
                if  tmp_sum == 0:
                    results.append([num, left_val, right_val])
                    left_ptr += 1
                    while nums[left_ptr] == nums[left_ptr - 1] and left_ptr < right_ptr:
                        left_ptr += 1
                elif tmp_sum > 0:
                    right_ptr -= 1
                else:
                    left_ptr += 1                
        return results