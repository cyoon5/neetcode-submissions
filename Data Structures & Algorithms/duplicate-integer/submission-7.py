class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = defaultdict(int)
        for i in range(len(nums)):
            if(hmap[nums[i]] == 0):
                hmap[nums[i]] = 1
            else:
                return True;
        return False;