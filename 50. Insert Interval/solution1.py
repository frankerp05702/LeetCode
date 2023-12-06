from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval and intervals:
            return intervals
        
        n = len(intervals)
        current_interval = []
        current_max = 0
        response = []
        newIntervalAppended = False
        for i,interval in enumerate(intervals):
            if not current_interval and interval[0] <= newInterval[0] and newInterval[0] <= interval[1]:
                # Found new overlap 
                current_interval = [interval[0]]
                current_max = max(current_max, interval[1])
                current_max = max(current_max, newInterval[1])
            elif not current_interval and newInterval[0] <= interval[0] and interval[0] <= newInterval[1]:
                # Found new overlap 
                current_interval = [newInterval[0]]
                current_max = max(current_max, interval[1])
                current_max = max(current_max, newInterval[1])
            elif current_max:
                if current_max >= interval[0]:
                    # Continue overlap
                    if current_max < interval[1] or current_max == interval[0]:
                        # Found end of overlap
                        current_interval.append(interval[1])
                        response.append(current_interval)
                        current_interval = []
                        current_max = 0
                        newIntervalAppended = True
                    else:
                        # Not found end of overlap. Overlap continues. Calculate max
                        current_max = max(current_max, interval[1])
                        current_max = max(current_max, newInterval[1])
                else:
                    # Found end of overlap
                    current_interval.append(current_max)
                    response.append(current_interval)
                    response.append(interval)
                    current_interval = []
                    current_max = 0     
                    newIntervalAppended = True       
            else: # No overlap
                if not newIntervalAppended and intervals[i - 1] < newInterval and newInterval < interval:
                    response.append(newInterval)
                    newIntervalAppended = True
                if i == 0:
                    if i == n - 1:
                        if interval[0] > newInterval[0]:
                            response.append(newInterval)
                            response.append(interval)
                        else:
                            response.append(interval)
                            response.append(newInterval)
                        newIntervalAppended = True
                    else:
                        if interval[0] > newInterval[0]:
                            response.append(newInterval)
                            newIntervalAppended = True
                        response.append(interval)
                elif i == n - 1:
                    if interval[0] < newInterval[0]:
                        response.append(interval)
                        response.append(newInterval)
                        newIntervalAppended = True
                    else:
                        response.append(interval)
                else:
                    response.append(interval)
            if i == n - 1 and current_max:
                    current_interval.append(current_max)
                    response.append(current_interval)
        return response


# Example 1:
intervals = [[1,3],[6,9]]
newInterval = [2,5]
expected = [[1,5],[6,9]]
s = Solution()
result = s.insert(intervals, newInterval)
print(result)
print(result == expected)

# Example 2:
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
expected = [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
s = Solution()
result = s.insert(intervals, newInterval)
print(result)
print(result == expected)

# Example 3: No intervals
intervals = []
newInterval = [2,5]
expected = [[2,5]]
s = Solution()
result = s.insert(intervals, newInterval)
print(result)
print(result == expected)

# Example 4: No newInterval and yes intervals.
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = []
expected = [[1,2],[3,5],[6,7],[8,10],[12,16]]
s = Solution()
result = s.insert(intervals, newInterval)
print(result)
print(result == expected)

# Example 5:
intervals = [[1,5]]
newInterval = [2,3]
expected = [[1,5]]
s = Solution()
result = s.insert(intervals, newInterval)
print(result)
print(result == expected)

# Example 6:
intervals = [[1,5]]
newInterval = [5,7]
expected = [[1,7]]
s = Solution()
result = s.insert(intervals, newInterval)
print(result)
print(result == expected)

# Example 7:
intervals = [[1,5]]
newInterval = [0,3]
expected = [[0,5]]
s = Solution()
result = s.insert(intervals, newInterval)
print(result)
print(result == expected)

# Example 8:
intervals = [[1,5]]
newInterval = [6,8]
expected = [[1,5],[6,8]]
s = Solution()
result = s.insert(intervals, newInterval)
print(result)
print(result == expected)

# Example 9:
intervals = [[0,2],[3,5],[6,8],[10,12],[13,15]]
newInterval = [4,7]
expected = [[0,2],[3,8],[10,12],[13,15]]
s = Solution()
result = s.insert(intervals, newInterval)
print(result)
print(result == expected)