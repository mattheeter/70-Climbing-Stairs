n = 5

def stairs(n):
    evenTrack = False
    # Based on the pattern, if n is between one and 3, the answer is n
    if n <= 3:
        return n
    # If the value is even, need to subtract one as last group does not follow pattern, and result should have one extra value
    if (n % 2) == 0:
        n -= 1
        result = 2
    else:
        # Starting at one as every number will have one grouping with n steps (all singles)
        result = 1
    # 
    

    return result
print(stairs(n))