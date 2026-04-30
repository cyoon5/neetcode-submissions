class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_stack = []
        for i in range(len(nums)):
            my_stack.append(nums[i])
        
        for i in range(len(my_stack)):
            if my_stack.pop() in my_stack:
             return True

        return False        
        
        
        