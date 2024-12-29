//Original solution: Meets average O(1) requirement but not the most efficient. 
class RandomizedSet {
    HashSet<Integer> set;
    public RandomizedSet() {
        this.set = new HashSet<Integer>(); 
    }
    
    public boolean insert(int val) {
        return this.set.add(val); 
    }
    
    public boolean remove(int val) {      
        return this.set.remove(val); 
    }
    
    public int getRandom() {  
        Integer[] values = set.toArray(new Integer[0]); 
        int random = (int) ((Math.random() * ((set.size()) - 0)) + 0);
        return values[random];
    }
}

//Better solution: Uses both a Hashmap and an ArrayList rather than a HashSet and the toArray() method. 
    HashMap<Integer, Integer> set; //Maps values to their index in values array. 
    ArrayList<Integer> values; 
    public RandomizedSet() {
        this.set = new HashMap<Integer, Integer>(); 
        this.values = new ArrayList<Integer>(); 
    }
    
    public boolean insert(int val) {
        if (this.set.containsKey(val)){
            return false; 
        } else {
            this.set.put(val, this.values.size()); 
            this.values.add(val); //Append to end.
            return true; 
        }
    }
    
    public boolean remove(int val) {    
        if (this.set.containsKey(val)){ 
            int idx = this.set.get(val); //Get the current idx to remove, expected O(1). 
            this.values.set(idx, this.values.get(this.values.size() - 1));  //Update values[idx] to be the last element in values, overwriting the thing we're removing.
            this.set.put(this.values.get(idx), idx); //Update the index of the replacing value in the hashmap. 
            this.set.remove(val); //Remove the value to remove from the hashmap.
            this.values.remove(this.values.size() - 1); //Remove the duplicate form the end of values. 
            return true; 
        } else {
            return false; 
        }  
    }
    
    public int getRandom() {  
        int random = (int) (Math.random() * this.values.size());
        return values.get(random); 

    }