//Original correct and efficient solution.
public boolean canConstruct(String ransomNote, String magazine) {
    if(ransomNote.length() > magazine.length()){
        return false; 
    }
    char letters[] = new char[26]; 
    for (int i = 0; i < magazine.length(); i++) {
        letters[magazine.charAt(i) - 'a']++; 
    }

    for (int i = 0; i < ransomNote.length(); i++) {
        if (letters[ransomNote.charAt(i) - 'a'] == 0){
            return false; 
        } else {
            letters[ransomNote.charAt(i) - 'a']--; 
        }
    }
    return true; 
}