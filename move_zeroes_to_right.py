class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        i = 0
        j = 0
        while j < len(arr):
            if arr[j] != 0:
                arr[i],arr[j] = arr[j],arr[i]
                i += 1
            j += 1


# [0 1 1 0 2 2 3 3] becomes [1 1 2 2 3 3 0 0 0] 