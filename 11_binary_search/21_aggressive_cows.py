class Solution:
    def can_place(self, stalls:list[int], cows:int, d:int):
        count = 1
        last_pos = stalls[0]

        for i in range(1, len(stalls)):
            # if stall is atleast d away from the last placed cow
            if stalls[i] - last_pos >= d:
               # place the cow here
               count+=1
               #update last position
               last_pos = stalls[i]
            #if all cows are placed
            if count >= cows:
                return True

        #could not place all cows
        return False
        
    def aggressive_cows(self, stalls: list[int], cows:int):
        stalls.sort()

        low = 1
        high = stalls[-1] - stalls[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            # if placement possible
            if self.can_place(stalls, cows, mid):
                # store answer
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
                