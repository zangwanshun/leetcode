class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        flip_dict = {'1':'0', '0':'1'}
        num_bin = bin(num)[2:]
        bin_list = []
        for letter in num_bin:
            bin_list.append(flip_dict[letter])
        bin_str = "".join(bin_list)
            
        return int(bin_str,2)
