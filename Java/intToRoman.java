//Super inefficient, but first correct solution.
   public String intToRoman(int num) {
        String roman = ""; 
        int places = 0;  

        HashMap<Integer, Character> map = new HashMap<>();
        map.put(0, '0'); 
        map.put(1, 'I'); 
        map.put(5, 'V'); 
        map.put(10, 'X'); 
        map.put(50, 'L'); 
        map.put(100, 'C'); 
        map.put(500, 'D');
        map.put(1000, 'M');  

        HashMap<Integer, String> subtractive = new HashMap<>(); 
        subtractive.put(4, "IV"); 
        subtractive.put(9, "IX"); 
        subtractive.put(40, "XL"); 
        subtractive.put(90, "XC"); 
        subtractive.put(400, "CD"); 
        subtractive.put(900, "CM"); 

        while (num > 0) {
            System.out.println(num); 
            String strNum = String.valueOf(num); 
            int power = (int) Math.pow(10, strNum.length() - 1); 
            int front = (int) (num / power); 
            int max = 0; 

            if (front != 4 && front != 9) {
                for (Integer i : map.keySet()) {
                    if (num - i >= 0 && i > max) {
                        max = i; 
                    }
                }

                Character symbol = map.get(max); 
                roman += symbol; 
                num -= max; 
            } else {
                String rep = subtractive.get(front * power); 
                roman += rep; 
                num -= (front * power); 
            }
            places--; 
        }

        return roman; 
}

//Better solution: O(n) time, O(1) space. 
public String intToRoman(int num) {
        String roman = ""; 
        int[] values = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
        String[] numerals = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"}; 
        int i = numerals.length - 1; 

        while (num > 0) {
            if (num < values[i]) {
                i--; 
            } else {
                roman += numerals[i]; 
                num -= values[i]; 
            }
        }
        return roman; 
}

//Another solution (note that this relies on the problem guarentee that 1 <= num <= 3999)
public String intToRoman(int num) {
    String[] ones = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}; 
    String[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}; 
    String[] hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}; 
    String[] thousands = {"", "M", "MM", "MMM"}; 

    String roman = ""; 
    roman += thousands[num / 1000];
    num -= (1000 * (num / 1000));  
    roman += hundreds[num / 100]; 
    num -= (100 * (num / 100));  
    roman += tens[num / 10]; 
    num -= (10 * (num / 10));  
    roman += ones[num];
    return roman; 
}