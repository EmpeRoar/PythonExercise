
def ArrayChallenge(arrayOfNumbers):
    n = arrayOfNumbers[0]
    arrayOfNumbers.pop(0)
    
    return str(n) + ' [' + ','.join(map(str, arrayOfNumbers)) + ']'

arrayOfNumber = [3, 1, 3, 5, 10, 6, 4, 3, 1]
print(ArrayChallenge(arrayOfNumber))


# [3], 1, 3, 5, 10, 6, 4, 3, 1
# 3 -- sliding window
# 1, 3, 5, 10, 6, 4, 3, 1 -- list of numbers

# 3, <-- sliding window size 1, 2, 3, 5, 6, 6, 4, 3
#  1, 3, 5                   = 3
#     3, 5, 10               = 5 
#        5, 6, 10            = 6  
#           4, 6, 10         = 6 
#               3, 4, 6      = 4
#                  1, 3, 4   = 3