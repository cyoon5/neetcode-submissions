class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        sol = []
        for i in range(n):
            j = i + 1
            count = 1 
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j+=1
                count+=1
            
            if j == n:
                count = 0
            sol.append(count)
        return sol

