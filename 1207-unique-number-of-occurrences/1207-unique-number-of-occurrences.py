class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lst = []
        arr1 = list(set(arr))
        for i in range(len(arr1)):
            x = arr.count(arr1[i])
            lst.append(x)
           # arr.remove(arr[i])
        if len(lst)==len(list(set(lst))):
            return True
        else:
            return False
        