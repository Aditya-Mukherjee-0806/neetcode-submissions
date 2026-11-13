class Solution {
    public boolean isAnagram(String s, String t) {
        int m = s.length(), n = t.length();
        int[] char_count = new int[26];
        for(int i = 0; i < m; i++)
            char_count[s.charAt(i) - 'a']++;
        for(int i = 0; i < n; i++)
            char_count[t.charAt(i) - 'a']--;
        for(int i = 0; i < 26; i++)
        {
            if(char_count[i] != 0)
                return false;
        }
        return true;
    }
}
