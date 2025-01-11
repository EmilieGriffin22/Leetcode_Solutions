//Original efficient and correct solution. 
bool isAnagram(char* s, char* t) {
    int letters[26]; 
    int i = 0;
    for (; s[i] != 0; i++){
        letters[s[i] - 'a']++; 
        if (!t[i]){
            return false; 
        }
        letters[t[i] - 'a']--;
    }

    if (t[i]){
        return false; 
    }

    for (int i = 0; i < 26; i++){
        if (letters[i]){
            return false; 
        }
    }

    return true;
    
}