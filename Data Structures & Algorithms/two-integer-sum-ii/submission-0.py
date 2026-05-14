class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since array is sorted in ascending order, we can get rid of all numbers >= to target

        p1 = 0
        p2 = len(numbers)-1

        while p1 < p2:
            if(numbers[p1] + numbers[p2] == target):
                return [p1+1, p2+1]
            if(numbers[p1] + numbers[p2] > target):
                p2-=1
            if(numbers[p1] + numbers[p2] < target):
                p1+=1
        
