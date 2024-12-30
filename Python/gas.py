#Original correct solution. 
def canCompleteCircuit(self, gas, cost):
    #Not enough gas on the route -- you must travel farther in a loop than there is avaialable gas.
    if (sum(gas) < sum(cost)): 
        return -1 

    #A solution is possible. 
    tank = 0
    start = 0 
    for i in range(len(gas)): 
        #Beginning at start, travel forward and save up extra gas. 
        tank += gas[i] - cost[i]
        if tank < 0: #If out of gas. 
            start = i + 1 #Start at the next position. 
            tank = 0 #Start with empty tank. 
    return start 