//Original correct (and efficient) solution. O(N) time and O(1) space. 
public boolean isSubsequence(String s, String t) {
        int i = 0; 
        int j = 0; 
        while (i < s.length() && j < t.length()){
            if (t.charAt(j) == s.charAt(i)){
                i++; 
            }

            j++;
        }
        return i == s.length(); 
}