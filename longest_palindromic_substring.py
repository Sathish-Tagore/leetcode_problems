class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=''
        def is_palin(st, l , r):
            while l >= 0 and r < len(st) and st[l] == st[r]:
                l -=  1
                r +=  1
            return st[l+1:r]
        for i in range(0,len(s)):
            len1 = is_palin(s,i,i)
            if len(len1) > len(longest) :
                longest = len1
            len2 = is_palin(s,i,i+1)
            if len(len2) > len(longest) :
                longest = len2 
        return longest
