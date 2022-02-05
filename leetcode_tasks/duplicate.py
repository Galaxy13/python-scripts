def containsDuplicate(nums) -> bool:
    temp_list = []
    i = 0
    while i < (len(nums) // 2) - 1:
        if nums[i] in temp_list or nums[-(i + 1)] in temp_list:
            return True
        else:
            temp_list.append(nums[i])
            temp_list.append(nums[-(i + 1)])
    return False


print(containsDuplicate([1, 2, 3, 4]))
