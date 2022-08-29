class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left_ptr = 0
        right_ptr = len(numbers) -1
        
        
        while left_ptr < right_ptr:
            
            left_val = numbers[left_ptr]
            right_val = numbers[right_ptr]
            sum = left_val + right_val
            
            if sum == target:
                return [left_ptr + 1, right_ptr + 1]
            elif sum > target:
                right_ptr -= 1
            else:
                left_ptr += 1