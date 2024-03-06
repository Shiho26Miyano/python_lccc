class Solution:
    # center expansion technique
    # o(n2), o(1)
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
    
    # sliding window
    # o(n2), o(1)
    def longestPalindrome2(self, s: str) -> str:
        if not s:
            return ""

        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes (expand around one center)
            odd_pal = expandAroundCenter(i, i)
            if len(odd_pal) > len(longest):
                longest = odd_pal

            # Even length palindromes (expand around two centers)
            even_pal = expandAroundCenter(i, i+1)
            if len(even_pal) > len(longest):
                longest = even_pal

        return longest