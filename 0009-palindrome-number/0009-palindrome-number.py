class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x)[::-1]
        return rev ==  str(x)
        