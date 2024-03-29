class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_nums = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}

        result = 0

        for i in range(len(s)-1):
            if roman_nums[s[i]] < roman_nums[s[i+1]]:
                result -= roman_nums[s[i]]
            else:
                result += roman_nums[s[i]]
        result += roman_nums[s[-1]]
        return result
