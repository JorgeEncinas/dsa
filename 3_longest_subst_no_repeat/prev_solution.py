class Solution(object):
    #A dictionary is an array with linked lists
    #If we use the same key, we'll end up in the same array space.
    #There, we could check the linked list and see the indexes.
    #You could just save a tuple (index of first occurrence, count)
    #Because the Hash Table array might be, say, of length 10
    #So two letters might share the same space.
    #Tuples are immutable, so I changed it to a list.

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        keys_dict = dict()
        len_s = len(s)
        sequence_len = 0
        count = 0
        index = 0
        sequence_ongoing = True
        while index < len_s:
            key = s[index]
            if key not in keys_dict:
                keys_dict[key] = [index, 0] #index is the very first occurrence on the current sequence
            keys_dict[key][1] += 1
            tupleX = keys_dict[key] #just for easier reference.
            if tupleX[1] > 1: #then it's repeated, and we should start back from after that one index
                if count > sequence_len: #Was our current sequence the biggest?
                    sequence_len = count
                count = 0 #start again
                sequence_ongoing = False
                index = int(tupleX[0]) #Reset to after the first instance of that letter. (index +=1 at the end)
                keys_dict.clear() #And remove all elements.
            else: #We're still going.
                count += 1
                sequence_ongoing = True
            index += 1
        if sequence_ongoing and count > sequence_len:
            sequence_len = count
        return sequence_len