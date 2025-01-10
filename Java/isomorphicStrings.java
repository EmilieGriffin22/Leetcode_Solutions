import java.util.HashMap; 
class Java {
    //Original time efficient solution using two arrays. 
    public boolean isIsomorphic(String s, String t) {
        char[] mapping = new char[257]; 
        boolean[] mapped = new boolean[257]; 
        for (int i = 0; i < s.length(); i++){
            if (mapping[s.charAt(i) + 1] == 0){
                if (mapped[t.charAt(i) + 1] == true) {
                    return false;
                }
                mapping[s.charAt(i) + 1] = t.charAt(i); 
                mapped[t.charAt(i) + 1] = true;
            } else if (mapping[s.charAt(i) + 1] != t.charAt(i)){
                return false; 
            }
        }
        return true; 
    }

    //Other solution using Hashmaps (less time efficient). 
    public boolean isIsomorphic2(String s, String t) {
        HashMap<Character, Character> mapping = new HashMap<>(); 
        HashMap<Character, Character> revMapping = new HashMap<>(); 
        for (int i = 0; i < s.length(); i++){
             if (!mapping.containsKey(s.charAt(i))){
                if (revMapping.containsKey(t.charAt(i))) {
                    return false;
                }
                mapping.put(s.charAt(i), t.charAt(i));
                revMapping.put(t.charAt(i), s.charAt(i));  
              } else if (mapping.get(s.charAt(i)) != t.charAt(i)){
                 return false; 
            }
         }
         return true; 
    }
}