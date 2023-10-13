class Solution(object):
       def findMedianSortedArrays(self, num1, num2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #Is this like doing merge sort? So that's why it would be O(log (m+n))?
        #Since they're already sorted, you don't need to do it *n* and *m* times, which is why it's not O(n, log n)
        i = 0
        j = 0
        arr = []
        while i < len(num1) and j < len(num2):
            if(num1[i] < num2[j]):
                arr.append(num1[i])
                i += 1
            else:
                arr.append(num2[j])
                j += 1
        if i < len(num1):
            #arr.append([num1[x] for x in range(i, len(num1))])
            for x in range(i, len(num1)):
                arr.append(num1[x])
        elif j < len(num2):
            for x in range(j, len(num2)):
                arr.append(num2[x])
        arr_len = len(arr)
        if arr_len % 2 != 0: #It has an exact center
            median = arr[int(((arr_len+1)/2)-1)]
        else: #No center, so sum the two closest.
            median = float(arr[int((arr_len/2)-1)] + arr[int((arr_len/2))])/2 
        return median