class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_letter_num, s2_letter_num = {}, {}
        index_l = 0
        for key in s1:
            try:
                s1_letter_num[key] += 1
            except KeyError:
                s1_letter_num[key] = 1

        for key2 in s2[:len(s1)]:
            try:
                s2_letter_num[key2] += 1
            except KeyError:
                s2_letter_num[key2] = 1

        for index_r in range(len(s1) - 1, len(s2)):
            if s1_letter_num == s2_letter_num:
                return True
            if index_r + 1 >= len(s2):
                return False
            else:
                s2_letter_num[s2[index_l]] -= 1
                if not s2_letter_num[s2[index_l]]:
                    s2_letter_num.pop(s2[index_l])
                try:
                    s2_letter_num[s2[index_r + 1]] += 1
                except KeyError:
                    s2_letter_num[s2[index_r + 1]] = 1
            index_l += 1
        return False
