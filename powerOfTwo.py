# Using Recursion
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return self.isPowerOfTwo(int(n/2))
        return False



#Using Bitwise Manipulation
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not(n & n -1)
   

'''
Runtime     Memory
38 ms       13.8 MB
45 ms       13.9 MB

'''



'''
s = Solution()
print(s.isPowerOfTwo(12))
print(s.isPowerOfTwo(11))
print(s.isPowerOfTwo(32))

False
False
True

'''

