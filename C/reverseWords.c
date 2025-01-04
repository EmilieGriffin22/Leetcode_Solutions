//Original correct (but inefficient) solution. 
void reverse(char *s, int start, int end){
    while(start < end){
        char temp = s[start]; 
        s[start] = s[end]; 
        s[end] = temp; 
        start++, end--;
    }
}


char* reverseWords(char* s) {
    //First need to remove any additional spaces from s. 
    int i = 0; 
    while(s[i] == ' '){
        s++; 
    }

    int len = strlen(s) - 1; 
    while(len >= 0 && s[len] == ' '){
        s[len] = 0;  
        len--; 
    }
    
    char *out = malloc(len + 2); 
    int p = 0;
    for (i = 0; s[i] != 0; i++){
        out[p] = s[i]; 
        p++;
        if(s[i + 1] == ' '){
            out[p] = s[i+1]; 
            p++; 
        }
        while (s[i + 1] == ' '){
            i++; 
        }
    }
    out[p] = 0; 

    //Now, p is currently the last index of out, which is s without extra space. 
    reverse(out, 0, p - 1);
    int startWord = 0; 
    int endWord = 0; 
    int w = 0; 
    for (int j = 0; j < p; j++){
        while(out[j] != ' ' && out[j] != 0){
            s[w++] = out[j++];
            endWord++;
        }
        reverse(s, startWord, endWord - 1); 
        s[w++] = ' '; 
        startWord = w; 
        endWord = startWord;
        
    }
    s[w - 1] = 0;
    
    return s; 
}

//Better solution.
void reverse(char *s, int start, int end){
    while(start < end){
        char temp = s[start]; 
        s[start] = s[end]; 
        s[end] = temp; 
        start++, end--;
    }
}


char* reverseWords(char* s) {
    //First need to remove any additional spaces from s. 
    while (s[0] == ' ') {
        s++;
    }

    int end = strlen(s) - 1; 
    while (end >= 0 && s[end] == ' ') {
        end--;
    }
    
    reverse(s, 0, end); 

    int wordStart = 0; 
    int wordEnd = 0; 
    for (int i =0 ; i <= end; i++){
        if(s[i] == ' ' || i == end){
            if (s[i] == ' '){
                wordEnd = i - 1; 
            } else {
                wordEnd = i; 
            }

            reverse(s, wordStart, wordEnd); 
            wordStart = i + 1; 
        }
    }

    int w = 0;
    for (int i = 0; i <= end; i++) {
        if (s[i] != ' ' || (i > 0 && s[i - 1] != ' ')) {
            s[w++] = s[i];
        }
    }

    s[w] = '\0';
    return s;
}