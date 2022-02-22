class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not(n & n -1)
      
'''
s = Solution()
print(s.isPowerOfTwo(12))
print(s.isPowerOfTwo(11))
print(s.isPowerOfTwo(32))

False
False
True

'''
