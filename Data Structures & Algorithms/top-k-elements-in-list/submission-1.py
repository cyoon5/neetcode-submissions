class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for n in nums:
            hmap[n] = hmap[n] + 1
        output = sorted(hmap, key = hmap.get,reverse = True)

    

        
        return output[0:k];

            
        