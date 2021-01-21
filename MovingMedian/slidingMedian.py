

def GetMedianOfCurrentSlidingWindow(slidingWindow):
    moduloOfSlidingWindow = len(slidingWindow) % 2
    if moduloOfSlidingWindow == 0:
        listOfMedians[0] = 0 # to be in the next video...
    else: 
        medianIndex = moduloOfSlidingWindow+1
        listOfMedians[currentMedianIndex] = slidingWindow[medianIndex]
        currentMedianIndex += 1        
    print(','.join(map(str, listOfMedians)))
    return

def GetNextSlidingWindow():
    currentIndex += 1
    slidingWindow = [0 for i in range(slidingWindowSize)]
    i = currentIndex
    x = 0
    while i < slidingWindowSize:
       slidingWindow[x] = listOfNumbers[i]
       x += 1
       i += 1

    GetMedianOfCurrentSlidingWindow(slidingWindow)
    GetNextSlidingWindow()
    return 

def GetCurrentWindow():
    global currentWindow
    global listOfMedians
    slidingWindow = [0 for i in range(slidingWindowSize)]
    i = currentIndex
    x = 0
    while i < slidingWindowSize:
       slidingWindow[x] = listOfNumbers[i]
       x += 1
       i += 1

    GetMedianOfCurrentSlidingWindow(slidingWindow)
    GetNextSlidingWindow()

def ArrayChallenge(arrayOfNumbers):
    global listOfNumbers
    global currentIndex
    global slidingWindowSize
    global currentMedianIndex

    currentMedianIndex = 0
    slidingWindowSize = arrayOfNumbers[0] # Sliding window Size
    arrayOfNumbers.pop(0)
    listOfNumbers = arrayOfNumbers
    
    global listOfMedians 
    listOfMedians = [len(listOfNumbers)]

    GetCurrentWindow()

    return ','.join(map(str, listOfMedians)) 

# ','.join(map(str, listOfNumbers))

currentWindow = []
listOfNumbers = []
currentIndex = 0
slidingWindowSize = 0
listOfMedians = []
currentMedianIndex = 0

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