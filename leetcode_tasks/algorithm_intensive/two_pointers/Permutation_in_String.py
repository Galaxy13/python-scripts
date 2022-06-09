class Solution:
    def permutations(self, string):
        if len(string) == 1:
            return string
        temp_list = []
        for perm in self.permutations(string[1:]):
            for index in range(len(string)):
                temp_list.append(perm[:index] + string[0:1] + perm[index:])
        return temp_list

    def checkInclusion_failed(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        index1, index2 = 0, len(s1) - 1
        s1_permutations = {perm: 1 for perm in self.permutations(s1)}
        while index2 <= len(s2):
            try:
                s1_permutations[s2[index1:index2 + 1]]
                return True
            except KeyError:
                index1, index2 = index1 + 1, index2 + 1
        return False
    # TODO: using all perms is not working

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        index1, index2 = 0, len(s1) - 1
        hash_s1 = 1
        for letter in s1:
            hash_s1 *= ord(letter)
        while index2 <= len(s2):
            hash_s2 = 1
            for letter in s2[index1:index2 + 1]:
                hash_s2 *= ord(letter)
            if 1 * hash_s2 == hash_s1:
                return True
            index1, index2 = index1 + 1, index2 + 1
        return False
