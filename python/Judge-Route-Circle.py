class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves_dict = {"R":(1,0),"L":(-1,0),"D":(0,-1),"U":(0,1)}
        origin = [0,0]
        for x in moves:
            origin[0],origin[1] = origin[0] + moves_dict[x][0], origin[1] + moves_dict[x][1]
        
        if origin == [0,0]:
            return True
        return False
