class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        i = 0
        j = 0
        while j < len(arr):
            val = arr[i]
            if arr[j] != val:
                arr[i+1] = arr[j]
                i += 1
            j += 1
        return i+1