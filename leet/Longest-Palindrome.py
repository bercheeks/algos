class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        mapping = {}
        for char in s:
            if mapping.get(char) == None:
                mapping[char] = 1
            else:
                mapping[char] += 1
        
        print(mapping)
        
        odd = False
        result = 0
        for key, item in mapping.items():
            if item % 2 == 1:
                odd = True
                result += item - 1
            else:
                result += item
        if odd == True:
            result += 1 
        return result 
