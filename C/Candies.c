//Original correct (but inefficient space) solution. 
//O(n) time and O(n) space. 
int candy(int* ratings, int ratingsSize) {
        int candies[ratingsSize]; 
        for (int i = 0; i < ratingsSize; i++) {
            if (i - 1 >= 0) {
                if (ratings[i] > ratings[i-1]){
                    candies[i] = candies[i - 1] + 1; 
                } else {
                    candies[i] = 1; 
                }
            } else {
                candies[i] = 1; 
            }
            
        }

        int s = candies[ratingsSize  - 1]; 
        for (int i = ratingsSize - 2; i >= 0; i--){
            if (ratings[i] > ratings[i+1] && candies[i] <= candies[i+1]){ 
                candies[i] = candies[i+1] + 1; 
            }
            s += candies[i]; 
        }
        return s; 
}

//Solution with optimal space. 
int candy(int* ratings, int ratingsSize) {
        int total_candy = ratingsSize; 
        int i = 1; 
        int child = 0; 
        int neighbor = 0; 

        while (i < ratingsSize) {
            //If child i has the same rating as child i - 1, no extra candies need to be allocated in turn.
            if (ratings[i] == ratings[i-1]){
                i++; 
                continue; 
            }

            child = 0; 
            //A child has a better rating than their neighbor and needs extra candy. 
            while (i < ratingsSize && ratings[i] > ratings[i-1]) {
                child++; //There is a child who needs more candy than peak currently was. 
                total_candy += child; //Give the child their candy. 
                i++; 
            }

            neighbor = 0; 
            //A child has a worse rating than their neighbor and their neighbor would need more candy.
            while (i < ratingsSize && ratings[i] < ratings[i-1]){
                neighbor++; //There is a neighbor who needs more candy than they have previously received. 
                total_candy += neighbor; //Give the neighbor their candy. 
                i++; 
            }

            //Too much candy may have been given out, as an index i is considered 2x as both a neighbor and child
            //When there is a turn around (i.e. as both i and i -1). In whatever siutaiton the child 
            //Was given less candy, take that amount away.  

            if (child > neighbor){
                total_candy -= neighbor; 
            } else {
                total_candy -= child; 
            }
        }

        return total_candy; 
}