class Solution {
    public boolean isAnagram(String s, String t) 
    {
        if(s.length() != t.length())
        return false;

 
        
        char[] sortS = new char[s.length()];
        char[] sortT = new char[t.length()];
        for(int i = 0; i < s.length(); i++)
        {
            sortS[i] = s.charAt(i);
            sortT[i] = t.charAt(i);
        }

        Arrays.sort(sortS);
        Arrays.sort(sortT);

        return Arrays.equals(sortS,sortT);
       
    }
}
