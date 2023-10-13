#Use an array as a stack with push and pop

class Solution(object):
    def getNormalMedian(self, arr):
        mustGetTwoValues = len(arr) % 2 == 0
        array_half = len(arr)/2
        return float((arr[array_half] + arr[array_half-1]) / 2.0) if mustGetTwoValues else float(arr[array_half])

    def getMedian(self, sorted_arr, isEven):
        if(len(sorted_arr) == 1):
            return sorted_arr[0]
        elif(len(sorted_arr) == 0):
            return 0
        elif(isEven):
            return float((sorted_arr[-1]+sorted_arr[-2])/2.0)
        else:
            return float(sorted_arr[-1]) if sorted_arr[-1]>sorted_arr[-2] else float(sorted_arr[-2])

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
        middle_point = (total_length/2)+1 if mustGetTwoValues else (total_length+1)/2
        sorted_arr = []
        print("num1: ", num1)
        print("num2: ", num2)
        print("Total_Length: ", {total_length})
        print("Must: ", mustGetTwoValues)
        print("middle_point: ", {middle_point})
        #if(len(num1) == 0 and len(num2) == 0):
        #    return 0.0
        #elif(len(num1) == 0):
        #    return self.getNormalMedian(num2)
        #elif(len(num2) == 0):
        #    return self.getNormalMedian(num1)
        steps = 0
        if(len(num1) == 0 and len(num2) == 0):
            return 0
        elif(len(num1) == 0):
            start = num2
            end = num1
        elif(len(num2) == 0):
            start = num1
            end = num2
        else:
            start = num1 if num1[0] < num2[0] else num2
            end = num2 if num1[0] < num2[0] else num1
        while(j < len(start) and steps < middle_point):
            print(f"j: {j}, i: {i}, steps: {steps}, middle point: {middle_point}")
            sorted_arr.append(start[j])
            print(f"appended: {start[j]}")
            steps +=1
            j += 1
            print(f"{i} < {len(end)} x and {steps} <= {middle_point}") #and {end[i]} <= {start[j]}
            while ((j >= len(start) and steps < middle_point) or (i < len(end) and steps < middle_point and end[i] <= start[j])):
                print(f"i: {i}, j: {j}, steps: {steps}, middle point: {middle_point}")
                print(f"appended: {end[i]}")
                sorted_arr.append(end[i])
                i+=1
                steps +=1
            
        print(f"sorted_arr: {sorted_arr}")
        return self.getMedian(sorted_arr, mustGetTwoValues)

if __name__ == "__main__":
    solution = Solution()
    #solved = solution.findMedianSortedArrays([1,3], [2])
    #solved = solution.findMedianSortedArrays([1, 2], [3, 4])
    solved = solution.findMedianSortedArrays([], [1])
    print(solved)
