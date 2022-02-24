"""
Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), find the minimum number of conference rooms required.

Sample I/O
Example 1
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2
Input: [[7,10],[2,4]]
Output: 1

"""
# Time:  O(nlogn)
# Space: O(n)

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {integer}
    def minMeetingRooms(self, intervals):
        starts, ends = [], []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1  # Acquire a room.
                s += 1
            else:
                cnt_rooms -= 1  # Release a room.
                e += 1
            # Update the min number of rooms.
            min_rooms = max(min_rooms, cnt_rooms)

        return min_rooms
