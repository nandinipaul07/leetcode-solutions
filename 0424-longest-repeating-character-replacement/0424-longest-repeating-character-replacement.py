class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        #the frequency of letters needed to be replaced= window length - most frequent char count

        count = {} #dictionary to track frequency of letters appearing in our window
        left = 0
        max_count = 0
        longest = 0


        for right in range (len(s)):
            char = s[right]

            if char not in count:
                count[char] = 0

            count[char] += 1

            max_count = max(max_count, count[char])

            window_len = right - left  + 1
            replacements = window_len - max_count

            if replacements > k:
                count[s[left]] -= 1
                left += 1

            window_len = right - left + 1
            longest = max(longest, window_len)

        return longest




