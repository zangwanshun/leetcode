class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        rnum = 0
        for i in J:
            rnum = rnum + S.count(i)
        return rnum
