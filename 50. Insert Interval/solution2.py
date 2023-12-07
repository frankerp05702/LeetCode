from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        # No sorting, intervals is already sorted.
        # intervals.sort()
        current_interval = []
        current_max = 0
        overlapped = []
        for i,interval in enumerate(intervals):
            current_max = max(current_max, interval[1])
            if i < n - 1 and current_max >= intervals[i + 1][0]:
                # Found an overlap with next interval
                if not current_interval: 
                    current_interval = [interval[0]]
            else: # No overlap with next interval
                if current_interval:
                    current_interval.append(current_max)
                    overlapped.append(current_interval)
                    current_interval = []
                    current_max = 0
                else:
                    overlapped.append(interval)
        return overlapped
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval and intervals:
            return intervals
        
        n = len(intervals)
        # Use binary search to find the correct insert index
        start, end, mid = 0, n, 0
        while end - start > 1:
            mid = (end - start)//2
            if newInterval < intervals[start + mid]:
                end = start + mid
            elif newInterval > intervals[start + mid]:
                start += mid

        
        insertIndex = -1
        if intervals[start][0] < newInterval[0]:
            insertIndex = start + 1
        elif intervals[start][0] > newInterval[0]:
            insertIndex = start
        else: # In case are equals, analize [1] position
            if intervals[start][1] > newInterval[1]:
                insertIndex = start
            else:
                insertIndex = start + 1
        # return
        # Insert newInterval and resolve overlap
        intervals.insert(insertIndex, newInterval)

        return self.merge(intervals)


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

# Example 10:
intervals = [[0,1],[5,5],[6,7],[9,11]]
newInterval = [12,21]
expected = [[0,1],[5,5],[6,7],[9,11],[12,21]]
s = Solution()
result = s.insert(intervals, newInterval)
print(result)
print(result == expected)

# Example 11:
intervals = [[2,3],[5,5],[6,6],[7,7],[8,11]]
newInterval = [6,13]
expected = [[2,3],[5,5],[6,13]]
s = Solution()
result = s.insert(intervals, newInterval)
print(result)
print(result == expected)

# Example 12:
intervals = [[3,6],[9,9],[11,13],[14,14],[16,19],[20,22],[23,25],[30,34],[41,43],[45,49]]
newInterval = [29,32]
expected = [[3,6],[9,9],[11,13],[14,14],[16,19],[20,22],[23,25],[29,34],[41,43],[45,49]]
s = Solution()
result = s.insert(intervals, newInterval)
print(result)
print(result == expected)

