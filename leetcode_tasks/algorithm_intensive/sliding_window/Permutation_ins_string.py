class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check_hash = {}
        match, index_l = 0, 0
        for letter in s1:
            check_hash[letter] = check_hash.get(letter, 0) + 1

        for index_r in range(len(s2)):
            try:
                check_hash[s2[index_r]] -= 1
                if not check_hash[s2[index_r]]:
                    match += 1
            except KeyError:
                pass

            if index_r - index_l >= len(s1):
                try:
                    if not check_hash[s2[index_l]]:
                        match -= 1
                    check_hash[s2[index_l]] += 1
                except KeyError:
                    pass
                index_l += 1

            if match == check_hash.values():
                return True
        return False

