class Solution:
    # Manacher's Algorithm
    # o(n), o(n)
    def longestPalindrome(self, s: str) -> str:
        s_prime = '#' + '#'.join(s) + '#'
        n = len(s_prime)
        palindrome_radii = [0] * n
        center = radius = 0
        
        for i in range(n):
            mirror = 2 * center - i

            if i < radius:
                palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])

            while (i + 1 + palindrome_radii[i] < n and 
                   i - 1 - palindrome_radii[i] >= 0 and
                   s_prime[i + 1 + palindrome_radii[i]] == s_prime[i - 1 - palindrome_radii[i]]):
                palindrome_radii[i] += 1

            if i + palindrome_radii[i] > radius:
                center = i
                radius = i + palindrome_radii[i]

        max_length = max(palindrome_radii)
        center_index = palindrome_radii.index(max_length)
        start_index = (center_index - max_length) // 2
        longest_palindrome = s[start_index: start_index + max_length]

        return longest_palindrome
    
    # center expansion technique
    # o(n2), o(1)
    def longestPalindrome_2(self, s: str) -> str:
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
            left += 1

            if end - start < right - left:
                start, end = left, right

        return s[start:end]
    
   