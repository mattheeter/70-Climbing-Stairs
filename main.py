n = 7

def stairs(n):
    # Based on the pattern, if n is between one and 3, the answer is n
    if n <= 3:
        return n
    # If the value is even, need to subtract one as last group does not follow pattern, and result should have one extra value
    if (n % 2) == 0:
        # Making result start one higher, as there will be a lone pair of all twos at the end
        result = 2
        # Don't want to loop through last elemetnt if even, as it will not follow the pattern
        length = range(n - 1)
    else:
        # Starting at one as every number will have one grouping with n steps (all singles)
        result = 1
        length = range(n)
    # Using for loop to calculate result
    for numTwos in length:
        # Finding the length of the current group
        groupLength = n - numTwos
        if groupLength > float(n)/2:
            break
        # Looping through the number of combinations until there's one that's equal to the number of stairs
        for num in range(2**groupLength):
            num = 

    return result
print(stairs(n))