class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        sortedNums = sorted(nums)

        for i in range(len(sortedNums)-2):
            j = i+1
            k = len(sortedNums)-1
            
            while j < k:
                if -sortedNums[i] == sortedNums[j] + sortedNums[k]:
                    t = [sortedNums[i], sortedNums[j], sortedNums[k]]
                    if t not in sol:
                        sol.append(t)
                    j+=1
                    k-=1
                elif -sortedNums[i] > sortedNums[j] + sortedNums[k]:
                    j += 1
                else:
                    k -= 1
        
        return sol