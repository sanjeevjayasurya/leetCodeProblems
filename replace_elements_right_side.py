# Given an array arr, replace every element in that array with the greatest element 
# among the elements to its right, and replace the last element with -1.

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        x = len(arr)-1
        n = 0
        while x > 0:
            if arr[x] > arr[x-1]:
                arr[x-1] = arr[x] 
            x -= 1
        while n < len(arr)-1:
            arr[n] = arr[n+1]
            n += 1
        arr[n] = -1 
        return arr