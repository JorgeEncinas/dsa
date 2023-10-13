#Use an array as a stack with push and pop

class Solution(object):
    def getNormalMedian(self, arr):
        mustGetTwoValues = len(arr) % 2 == 0
        array_half = len(arr)/2
        return float((arr[array_half] + arr[array_half-1]) / 2.0) if mustGetTwoValues else float(arr[array_half])

    def getMedian(self, value1, value2, isEven):
        if(isEven):
            return float((value1+value2)/2.0)
        else:
            return float(value1) if value1>value2 else float(value2)

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
        total_length = len(num1)+len(num2)
        mustGetTwoValues = total_length % 2 == 0
        top_value = (total_length/2)+1 if mustGetTwoValues else (total_length+1)/2
        sorted_arr = []
        print("num1: ", num1)
        print("num2: ", num2)
        print("Total_Length: ", {total_length})
        print("Must: ", mustGetTwoValues)
        print("top_value: ", {top_value})
        if(len(num1) == 0 and len(num2) == 0):
            return 0.0
        elif(len(num1) == 0):
            return self.getNormalMedian(num2)
        elif(len(num2) == 0):
            return self.getNormalMedian(num1)
        steps = 0
        value_at_num1 = 0
        value_at_num2 = 0
        while(steps <= top_value):
            print(f"Steps: {steps}, i:{i}, j:{j} | v1:{value_at_num1}, v2:{value_at_num2}")
            #While we haven't surpassed the top value...
            if (mustGetTwoValues and steps == top_value):
                value1 = sorted_arr.pop()
                value2 = sorted_arr.pop()
                print("going into getMedian: %d, %d" % (value1, value2))
                median = self.getMedian(value1, value2, True)
                print(F"MEDIAN: {median}")
                return median
            elif (steps == top_value):
                value1 = sorted_arr.pop()
                value2 = sorted_arr.pop()
                print("going into getMedian uneven: %d, %d" % (value1, value2))
                median = self.getMedian(value1, value2, False)
                print(F"MEDIAN: {median}")
                return median
            value_at_num1 = num1[i]
            value_at_num2 = num2[j]
            if(value_at_num1 == value_at_num2):
                print(f"value1: {value_at_num1} = value2: {value_at_num2}")
                if(num1[i+1] <= num2[j+1]):
                    print(f"Picked value 1 on equal{value_at_num1}")
                    sorted_arr.append(value_at_num1)
                    i+=1
                else:
                    print(f"Picked value 2 on equal {value_at_num2}")
                    sorted_arr.append(value_at_num2)
                    j+=1
            if (i < len(num1) and value_at_num1 < value_at_num2):
                print(f"Picked value 1: {value_at_num1} | {value_at_num1} vs {value_at_num2}")
                sorted_arr.append(value_at_num1)
                i += 1
            elif(j <= len(num2)):
                print(f"Picked value 2: {value_at_num2} | {value_at_num1} vs {value_at_num2}")
                sorted_arr.append(value_at_num2)
                j += 1
            steps +=1

if __name__ == "__main__":
    solution = Solution()
    solution.findMedianSortedArrays([1,2], [3, 4])
