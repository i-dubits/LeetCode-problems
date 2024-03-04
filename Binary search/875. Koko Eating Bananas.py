class Solution:

    def current_k_time(self, k):
        h_res = 0
        for pile in self.piles:
            if pile <= k:
                h_res += 1
            else:
                h_res += pile // k
                if pile % k != 0:
                    h_res += 1
        return h_res

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        self.piles = piles
        k_min = 1
        k_max = max(self.piles)

        if len(self.piles) == 1:
            k_cand = self.piles[0] // h
            k_cand = k_cand if self.piles[0] % h == 0 else k_cand + 1
            return k_cand


        while k_min < k_max:

            if k_max == k_min + 1:
                time_current_1 = self.current_k_time(k_max)
                time_current_2 = self.current_k_time(k_min)
                if time_current_1 <= h and time_current_2 <= h and time_current_1 >= time_current_2:
                    k_curr = k_max
                elif time_current_1 <= h and time_current_2 <= h and time_current_2 >= time_current_1:
                    k_curr = k_min
                elif time_current_1 <= h:
                    k_curr = k_max
                else:
                    k_curr = k_min
                return k_curr

            k_curr = k_min + (k_max - k_min) // 2
            time_current = self.current_k_time(k_curr)
            if time_current > h:
                k_min = k_curr
            else:
                k_max = k_curr

        return k_curr





# piles = [3,6,7,11]
# h = 8
# piles = [11312884470]
# h = 968709470
piles = [2, 2]
h = 4
# piles = [30,11,23,4,20]
# h = 5
# piles = [30,11,23,4,20]
# h = 6

sol = Solution()

#print(sol.current_k_time(2))

print(sol.minEatingSpeed(piles, h))