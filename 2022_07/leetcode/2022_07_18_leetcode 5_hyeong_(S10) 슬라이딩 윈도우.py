class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        if len(s) < 2 or s == s[::-1]:
            return s
        def fun1(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s) - 1):
            result = max(result, fun1(i, i + 1), fun1(i, i + 2), key=len)
        return result

b = Solution()
a = ["babad", "cbbd"]


for i in a:
    print(b.longestPalindrome(i))