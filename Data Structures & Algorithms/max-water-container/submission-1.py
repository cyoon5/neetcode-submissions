class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maxWater = 0

        while i < j:
            if (j-i) * min(heights[i], heights[j]) > maxWater:
                maxWater = (j-i) * min(heights[i], heights[j])
            if(heights[i] > heights[j]):
                j-=1
            elif(heights[j] > heights[i]):
                i+=1
            else:
                j-=1
                i+=1
        return maxWater

            
