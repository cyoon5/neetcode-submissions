class Solution:
    def search(self, nums: List[int], target: int) -> int:

        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            split = p1 + (p2-p1)//2

            if nums[split] > target:
                p2 = split - 1
            elif nums[split] < target:
                p1 = split + 1
            else: 
                return split
        return -1

