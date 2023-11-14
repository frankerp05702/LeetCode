from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        total_gas, current_gas, start_index = 0, 0, 0

        for i in range(n):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            if current_gas<0:
                current_gas = 0
                start_index = i + 1

        return start_index if total_gas>=0 else -1
                

# Example 1:

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.

s=Solution()
print(s.canCompleteCircuit(gas,cost))

# Example 2:

gas = [2,3,4]
cost = [3,4,3]

s=Solution()
print(s.canCompleteCircuit(gas,cost))

# Example 3:

gas = [3,1,1]
cost = [1,2,2]

s=Solution()
print(s.canCompleteCircuit(gas,cost))

# Example 4:

gas = [2]
cost = [2]

s=Solution()
print(s.canCompleteCircuit(gas,cost))