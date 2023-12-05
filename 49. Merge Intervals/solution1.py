from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
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

# Example 1:
intervals = [[1,3],[2,6],[8,10],[15,18]]
expected = [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
s = Solution()
result = s.merge(intervals)
print(result)
print(result == expected)

# Example 2:
intervals = [[1,4],[4,5]]
expected = [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
s = Solution()
result = s.merge(intervals)
print(result)
print(result == expected)

# Example 3:
intervals = [[1,4],[0,4]]
expected = [[0,4]]
s = Solution()
result = s.merge(intervals)
print(result)
print(result == expected)

# Example 4:
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
expected = [[1,10]]
s = Solution()
result = s.merge(intervals)
print(result)
print(result == expected)

