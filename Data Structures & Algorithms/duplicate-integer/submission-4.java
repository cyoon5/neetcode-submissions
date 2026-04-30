class Solution 
{
    public boolean hasDuplicate(int[] nums) 
    {
        HashMap<Integer, Integer> x = new HashMap<Integer, Integer>();

        for(int i = 0; i < nums.length; i++)
        {
            if(x.containsKey(nums[i])){
                return true;
            }
            else{
                x.put(nums[i], 2);
            }
        }
        
        return false;
    }
}