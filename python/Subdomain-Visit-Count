class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict_return = {}
        for cpdomain in cpdomains:
            count,domain = cpdomain.split(" ")
            dot_left = domain.find(".")
            dot_right = domain.rfind(".")
            if dot_left != dot_right:
                dict_return[domain[dot_left+1:]] = dict_return.get(domain[dot_left+1:],0) + int(count)
            dict_return[domain[dot_right+1:]] = dict_return.get(domain[dot_right+1:],0) + int(count)
            dict_return[domain] = dict_return.get(domain,0) + int(count)
        
        list_return = [(str(x[1])+" "+str(x[0])) for x in dict_return.items()]
        return list_return
