class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        holder = {}
        indices: list[int] = []
        for i in range(len(nums)):
            difference = target-nums[i]
            if not holder.get(difference) and holder.get(difference) != 0:
                holder[nums[i]] = i
            else:
                indices.append(i)
                indices.append(holder[difference])
        return sorted(indices)
        