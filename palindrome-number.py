class Solution(object):
    def isPalindrome(self, 121):
        
        rev = 0
        while (121>0):
            rev = (rev* 10) + (121 % 10)
            121 = 121//10        
            
        return (rev == 121)
    
        