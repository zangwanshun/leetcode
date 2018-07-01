class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 0 
        units = 0
        MAX_UNITS = 100
        for letter in S:
            now_units =  widths[ord(letter) - ord('a')]
            if (now_units + units) > MAX_UNITS:
                lines += 1
                units = now_units
            else:
                units += now_units
        lines += 1
        return lines,units
