class Solution 
{
    public boolean hasDuplicate(int[] nums) 
    {
        Stack<Integer> s = new Stack<>();

        for(int i = 0; i < nums.length; i++)
        {
            s.push(nums[i]);
        }

        while(!s.isEmpty())
        {
            if(s.contains(s.pop()))
            return true;
        }
        return false;
        
    }
}