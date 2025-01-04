//Original correct (and efficient) solution. 
int strStr(char* haystack, char* needle) {
        for (int i = 0; haystack[i] != 0; i++){ 
            int j = i;
            while (haystack[j] && needle[j - i] && haystack[j] == needle[j - i]){
                j++;
            }
            if (!needle[j-i]){ 
                return i;
            }
        }
        return -1;
}