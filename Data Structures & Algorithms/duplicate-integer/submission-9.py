class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hmap = {}
        for i in range(n):
            if hmap.get(nums[i]) is not None:
                return True
            hmap[nums[i]] = i
        
        return False