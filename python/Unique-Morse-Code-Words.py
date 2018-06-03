class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet_table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        words2alphabet_set = set()
        for word in words:
            alphabet = [ alphabet_table[ord(letter) - ord('a') ] for letter in word ]
            words2alphabet = "".join(alphabet)
            words2alphabet_set.add(words2alphabet)
        return len(words2alphabet_set)
