class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        distance_return = []
        for index in range(0,len(S)):
            distance_left = S[index:].find(C)
            distance_right = S[index::-1].find(C)
            if distance_left < 0:
                distance_return.append(distance_right)
            elif distance_right < 0:
                distance_return.append(distance_left)
            else:
                distance_return.append(min(distance_left,distance_right))
        return distance_return
            
#map( lambda x:min(map(lambda y:abs(x-y),filter(lambda z:S[z] == C,range(len(S))) )),range(len(S)))
