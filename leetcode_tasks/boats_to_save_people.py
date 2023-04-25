from typing import List
class Solution:
    @staticmethod
    def numRescueBoats(people: List[int], limit: int) -> int:
        people.sort()
        boats_count = 0
        l, r = 0, len(people) - 1
        while l <= r:
            if people[r] + people[l] > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            boats_count += 1
        return boats_count


people = [3,2,2,1]
limit = 3
print(Solution.numRescueBoats(people, limit))