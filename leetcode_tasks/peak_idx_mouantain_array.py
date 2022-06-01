class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        if len(arr) == 2:
            return arr.index(max(arr))
        middle_idx = len(arr) // 2
        if arr[middle_idx - 1] < arr[middle_idx] > arr[middle_idx + 1]:
            return middle_idx
        else:
            if arr[middle_idx - 1] < arr[middle_idx]:
                return middle_idx + self.peakIndexInMountainArray(arr[middle_idx:])
            return self.peakIndexInMountainArray(arr[:middle_idx])