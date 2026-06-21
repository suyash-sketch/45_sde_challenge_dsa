class Solution:
    def max_meetings(self, start : list[int], end: list[int]):
         meetings = [(end[i], start[i], i + 1) for i in range(len(start))]
    
        #store by end time
        meetings.sort()

        result = []
        last_end = -1

        for e,s, idx in meetings:
            if s > last_end:
                result.append(idx)
                last_end = e


        return result
