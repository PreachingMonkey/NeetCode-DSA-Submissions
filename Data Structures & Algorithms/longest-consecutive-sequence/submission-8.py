class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current_Counter=1
        max_Counter=1
        num = sorted(set(nums))
        if len(num)==0:
            max_Counter=0
            return max_Counter
        for i in num:
            if i+1 in num:
                current_Counter += 1
            else:
                current_Counter = 1

            if current_Counter>=max_Counter:
                max_Counter = current_Counter
        
        return max_Counter