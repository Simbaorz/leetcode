"""
give a integer randomly, judge if it suit power of three
"""

import math

__metaclass__ = type
__author__ = 'Simba'


class Solution:

    def isPowerOfThree(self, n):
        if n < 0:
            return False

        if math.pow(3, (int)(math.log(0xFFFFFFFF, 3.0))) % n == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    for i in xrange(1, 101):
        print i, s.isPowerOfThree(i)
