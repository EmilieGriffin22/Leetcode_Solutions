//Original correct (but non-optimal) solution. 
//Beats 100% on runtime and 35% on memory. 
int maxProfit(int* prices, int pricesSize) {
    int buy, sell, maxProfit, currProfit; 
    maxProfit = currProfit = 0; 
    buy = prices[0]
    sell = 1; 
    while (sell < pricesSize){
        int profit = prices[sell] - buy; 
        if (profit > currProfit){
            currProfit = profit; 
            sell++; 
        } else { //Move on! 
            maxProfit += currProfit; 
            buy = prices[sell]; 
            sell++; 
            currProfit = 0; 
        }
    }

    if (currProfit > 0){
        maxProfit += currProfit; 
    }

    return maxProfit; 
}

//Optimized solution (greedy). 
//Still O(n) time and O(1) space but less variables. A more elegant solution derived from my original. 
int maxProfit(int* prices, int pricesSize) {
    int profit = 0; 
    for (int i = 1; i < pricesSize; i++){
        if (prices[i] - prices[i - 1] > 0){
            profit += prices[i] - prices[i - 1]; 
        }
    }
    return profit; 
}
