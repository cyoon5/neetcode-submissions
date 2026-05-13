class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        candidates = set()

        longest = 0

        for n in nums:
            if(n-1 not in numset):
                candidates.add(n)
        
        for n in numset:
            if n in candidates:
                length = 1
                while(n + length) in numset:
                    length+=1
                longest = max(length, longest)
        
        return longest
            



