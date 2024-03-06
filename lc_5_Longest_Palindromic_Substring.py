class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        for i in range(len(s)):
            c = s[i]
            left, right = i, i

            while left >= 0 and s[left] == c:
                left -= 1
            while right < len(s) and s[right] == c:
                right += 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # Adjust left index because we moved one step too far in the last loop
            left += 1

            if end - start < right - left:
                start, end = left, right

        # Python's slicing includes the start index and excludes the end index, similar to Java's substring
        return s[start:end]
