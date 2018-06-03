class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        binary_list = [1,0]
        for matrix_out in A:
            out_len = len(matrix_out)
            for x in range(0,(out_len+1)/2):
                matrix_out[x],matrix_out[out_len-x-1] = matrix_out[out_len-x-1],matrix_out[x]
                matrix_out[x],matrix_out[out_len-x-1] = binary_list[matrix_out[x]],binary_list[matrix_out[out_len-x-1]]
            
        return A
