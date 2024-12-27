
//Original correct solution. 
//O(n) time complexity, O(1) space.
//But, does not fair well compared to other LeetCoders. 
int maxProfit(int* prices, int pricesSize) {
    int buy, sell, maxProfit; 
    buy = maxProfit = 0; 
    sell = 1; 
    while (sell < pricesSize){
        int profit = prices[sell] - prices[buy]; 
        if (profit > 0){
            sell++; 
            if (profit > maxProfit) {
                maxProfit = profit; 
            }
        } else {
            buy = sell; 
            sell++; 
        }

    }
    return maxProfit; 
}

//Improves on runtime by getting rid of unessecary array accesses (beats 100% on runtime). 
int maxProfit(int* prices, int pricesSize) {
    int buy, sell, maxProfit; 
    maxProfit = 0; 
    buy = prices[0]; 
    sell = 1; 
    while (sell < pricesSize){
        int profit = prices[sell] - buy; 
        if (profit > 0){
            sell++; 
            if (profit > maxProfit) {
                maxProfit = profit; 
            }
        } else {
            buy = prices[sell]; 
            sell++; 
        }

    }
    return maxProfit; 
}