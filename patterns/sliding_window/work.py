global_arr = [1, 2, 3, 4, 5, 6]
# 6 - 1 Determining how many steps there are available is a function of the window size and the size of the array. A window size = array_size allows for 1 pass.
# 5 - 2 The bigger the window, the less passes. The smaller the window, the more passes. So it's an inversely proportional thing.
# 3 - 4

# (array_size % window_size) + 1 I think gives you the amout of steps
# Not true, since 6 / 3 = 0, + 1 = 1
#The guy does len(arr)-k+1

def findAllSubarraySums(k):
    sums = []
    initial_sum = 0
    for index in range(0, k):
        initial_sum += global_arr[index]
    sums.append(initial_sum)
    steps = len(global_arr)-k+1 #-1 bc we've covered the very first one. But not really, since we're starting at 1.
    print(f"steps: {steps}")
    for index in range(1, steps):
        #print(index+k)
        initial_sum = initial_sum - global_arr[index-1] + global_arr[index+(k-1)]
        sums.append(initial_sum)
        print(f"index: {index}, k: {k}. {global_arr[index:index+k]}")
    return sums
#0, 1, 2
#3, 6-1=5
#You require only one pass through the array, so that's O(N). But what if you had to print the whole thing? What then?
#You would have to keep the current subarray somehow, right?

def findSumShortestSubarray(target):
    #Find a value that >= target
    min_window_size = 9999
    subarrays_all = []
    chosen_values = []
    left_pointer = 0
    right_pointer = 0 #Must be at least two elements
    window_size = 1
    #PRECOMPUTE FIRST SUM
    accumulated_sum = 0
    isRightPointersTurn = True
    for index in range(0, window_size):
        accumulated_sum += global_arr[index]
    if (accumulated_sum >= target): #You could return at this point, saving yourself the "while" part.
        chosen_values = global_arr[left_pointer:right_pointer]
        min_window_size = window_size
        subarrays_all.append(global_arr[left_pointer:right_pointer+1])
        #isRightPointersTurn = False 
    print(f"Left: {left_pointer}, Right: {right_pointer}")
    while(left_pointer <= len(global_arr)-2): #So it requires two passes through the array, O(2N) -> O(N) [1, 2, 3, 4, 5]
        #First move one step, then subtract/add
        if (isRightPointersTurn and right_pointer <= len(global_arr)-1):
            right_pointer += 1
            window_size += 1
            accumulated_sum += global_arr[right_pointer]
            if (accumulated_sum >= target):
                subarrays_all.append(global_arr[left_pointer:right_pointer+1])
                if(window_size <= min_window_size): #(right_pointer-left_pointer)
                    min_window_size = window_size
                    chosen_values = global_arr[left_pointer:right_pointer+1]
                isRightPointersTurn = False
        else:
            left_pointer += 1
            window_size -= 1
            accumulated_sum -= global_arr[left_pointer-1]
            if(accumulated_sum >= target):
                subarrays_all.append(global_arr[left_pointer:right_pointer+1])
                if(window_size <= min_window_size):
                    min_window_size = window_size
                    chosen_values = global_arr[left_pointer:right_pointer+1]
            if(left_pointer == right_pointer):
                isRightPointersTurn = True
        print(f"Left: {left_pointer}, Right: {right_pointer}")
    for subarray in subarrays_all:
        print(subarray)  
    print(f"FINAL: {chosen_values}, MIN_LENGTH: {min_window_size}")


#Here's "Byte by Byte"'s implementation https://www.youtube.com/watch?v=GcW4mgmgSbw
#FIXED WINDOW
def fixed_sliding_window(arr, k):
    curr_subarray = sum(arr[:k])
    result = [curr_subarray]
    for i in range(1, len(arr)-k+1):
        curr_subarray = curr_subarray - arr[i-1]
        curr_subarray = curr_subarray + arr[i+k-1]
        result.append(curr_subarray)
    
    return result

#DYNAMIC-SIZE SLIDING WINDOW
def dynamic_sliding_window(arr, x): #[1, 2, 3, 4, 5, 6]
    min_length = float('inf')
    start = 0
    end = 0
    curr_sum = 0

    while end < len(arr):
        curr_sum = curr_sum + arr[end]
        end += 1

        while start < end and curr_sum >= x:
            curr_sum = curr_sum - arr[start]
            start += 1

            min_length = min(min_length, end-start+1)
        
        return min_length

#It's a much cleaner-looking solution.
# Let's write down the differences.
# First, they never check while the window's getting bigger per se.
# I think the "min(min_length, end-start+1)" requires that +1, because it's first deleting that element and diminishing the length
# So it is compensating for that.

# I'll try to write it out from just having that quick glance.

def dsw(target):
    arr = [1, 2, 3, 4, 5, 6]
    start = 0
    end = 0
    min_len = 9999999999
    curr_sum = 0

    while (end < len(arr)):
        curr_sum += arr[end]
        end+=1
        while start<end and curr_sum >= target:
            min_len = min(min_len, end-start)
            curr_sum -= arr[start]
            start -= 1
        
    print(f"sum: {curr_sum}, min_len: {min_len}")

#And that's it. How elegant a solution.

if __name__ == "__main__":
    #resultFixedSW = findAllSubarraySums(k=3)
    resultDynamicSW = findSumShortestSubarray(7)
    #print(resultFixedSW)