
def two_sum1(nums, target):
    #TWO-PASS HASH TABLE. RETURN THE INDICES OF THE TWO NUMBERS THAT ADD UP TO "TARGET"
    value_index_dict = {}
    for (index, value) in enumerate(nums):
        value_index_dict[value] = index
    for (index, value) in enumerate(nums):
        if(value_index_dict.get((target-value)) is not None):
            return [index, value_index_dict[target-value]]

def two_sum2(nums, target):
    #ONE-PASS HASH TABLE. RETURN THE INDICES OF THE TWO NUMBERS THAT ADD UP TO "TARGET"
    value_index_dict = {}
    for (index, value) in enumerate(nums):
        if(value_index_dict.get(target-value) is not None):
            return [index, value_index_dict[(target-value)]]
        else:
            value_index_dict[value] = index


if __name__ == "__main__":
    #result = two_sum1([1, 2, 3, 4, 5], 7)
    result2 = two_sum2([1, 2, 3, 4, 5], 7)
    print(result2)