    //Original correct and efficient (but complex) solution. 
    public int romanToInt(String s) {
        int ret = 0; 
        for (int i = 0; i < s.length(); i++){
            char curr = s.charAt(i); 
            switch (curr) {
                case 'I' : 
                    if (i + 1 < s.length() && s.charAt(i+1) == 'V') {
                        ret += 4; 
                        i++; 
                        break; 
                    } else if (i + 1 < s.length() && s.charAt(i+1) == 'X') {
                        ret += 9; 
                        i++; 
                        break; 
                    } else {
                        ret += 1; 
                        break; 
                    }
                case 'V' : 
                    ret += 5;
                    break; 
                case 'X' : 
                    if (i + 1 < s.length() && s.charAt(i+1) == 'L') {
                        ret += 40; 
                        i++;
                        break; 
                    } else if (i + 1 < s.length() && s.charAt(i+1) == 'C') {
                        ret += 90; 
                        i++;
                        break; 
                    } else {
                        ret += 10; 
                        break; 
                    }
                case 'L' : 
                    ret += 50; 
                    break; 

                case 'C' : 
                    if (i + 1 < s.length() && s.charAt(i+1) == 'D') {
                        ret += 400; 
                        i++;
                        break; 
                    } else if (i + 1 < s.length() && s.charAt(i+1) == 'M') {
                        ret += 900; 
                        i++;
                        break; 
                    } else {
                        ret += 100; 
                        break; 
                    }

                case 'D' : 
                    ret += 500; 
                    break; 

                default : 
                    ret += 1000;
                    break; 
            }

        }
        return ret; 
    }

//Solution using a HashMap. Not as efficient (extra space and time), but simplier. 
public int romanToInt(String s) {
        int ret  = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        map.put('0', 0); 
        map.put('I', 1); 
        map.put('V', 5); 
        map.put('X', 10); 
        map.put('L', 50); 
        map.put('C', 100); 
        map.put('D', 500);
        map.put('M', 1000);  
        
        for (int i = 0; i < s.length(); i++) {
            Character curr1 = s.charAt(i); 
            Character curr2 = '0';
            if (i + 1 < s.length()) {
                curr2 = s.charAt(i+1); 
            }

            int val1 = map.get(curr1); 
            int val2 = map.get(curr2); 

            if (val1 >= val2) {
                ret += val1; 
            } else {
                ret += (val2 - val1); 
                i++; 
            }
        }

        return ret; 
}
