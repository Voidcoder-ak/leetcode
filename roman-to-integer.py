class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        
        x = len(s)
        total = 0
        
        for i in range(0, x-1):
            if roman[s[i]] < roman[s[i+1]]:
                total = total - roman[s[i]]
            else:
                total = total + roman[s[i]]
        
        total = total + roman[s[x-1]]
        
        return total