from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        left, right = 0, len(p) - 1
        hash_slide = {}
        hash_p = {}
        ret_list = []
        while left <= right:
            try:
                hash_slide[s[left]] += 1
            except KeyError:
                hash_slide[s[left]] = 1
            try:
                hash_p[p[left]] += 1
            except KeyError:
                hash_p[p[left]] = 1
            left += 1
        left = 0
        while right < len(s):
            if hash_p == hash_slide:
                ret_list.append(left)
            hash_slide[s[left]] -= 1
            if not hash_slide[s[left]]:
                hash_slide.pop(s[left])
            left += 1
            right += 1
            if right < len(s):
                if s[right] in hash_slide.keys():
                    hash_slide[s[right]] += 1
                else:
                    hash_slide[s[right]] = 1
        return ret_list


if __name__ == '__main__':
    print(Solution().findAnagrams(s="abab",
                                  p="ab"))
