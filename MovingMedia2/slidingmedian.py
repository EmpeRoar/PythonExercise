"""
Have the function ArrayChallenge(arr) read the array of numbers stored in arr which will 
contain a sliding window size, N, as the first element in the array and the rest will be a 
list of numbers. 
Your program should return the Moving Median for each element based on the 
element and its N-1 predecessors, where N is the sliding window size. 
The final output should 
be a string with the moving median corresponding to each entry in the original array separated by commas.
Note that for the first few elements (until the window size is reached), the median is computed 
on a smaller number of entries. 
For example: if arr is [3, 1, 3, 5, 10, 6, 4, 3, 1] then your program should output "1,2,3,5,6,6,4,3"
Input: new int[] {5, 2, 4, 6}
Output: 2,3,4
Input: new int[] {3, 0, 0, -2, 0, 2, 0, -2}
Output: 0,0,0,0,0,0,0

[3],  - n sliding window size
1, 3, 5, 10, 6, 4, 3, 1 - list of numbers
                             1
                             2 
1,3,5                     =  3
  3,5,10                  =  5
    5,10,6    (5,6,10)    =  6
      10,6,4  (4,6,10)    =  6
         6,4,3 (3,4,6)    =  4
           4,3,1 (1,3,4)  =  3 

5,6,7,8
6, 7 

"""

def GetMedianOfSlidingWindow(currentSlidingWindow):
    mod = len(currentSlidingWindow) % 2
    slidingMedianVal = 0
    if mod != 0:
       slidingMedian = mod;        
       return currentSlidingWindow[slidingMedian]  
    else:      
       i1 = currentSlidingWindow / 2
       i2 = i1 + 1
       return currentSlidingWindow[i1-1]  + currentSlidingWindow[i2-1] / 2
    
def GetNextSlidingWindow(listOfMedian, listOfNumber, slidingWindowSize, currentIndex):
    currentSlidingWindow = []
    i = currentIndex
    while i < (slidingWindowSize+currentIndex):
        currentSlidingWindow.append(listOfNumber[i]) 
        i += 1
    try:
        currentSlidingWindow.sort()
        median = GetMedianOfSlidingWindow(currentSlidingWindow)
        listOfMedian.append(median) 
        currentIndex += 1
        GetNextSlidingWindow(listOfMedian, listOfNumber, slidingWindowSize, currentIndex)           
        return
    except:
        return
    
def ArrayChallenge(arr):
    slidingWindowSize = arr[0]
    arr.pop(0)
    listOfNumber = arr
    i = 0
    medianIndex = 1
    listOfMedian = []
    while medianIndex < slidingWindowSize:
        listOfMedian.append(medianIndex)
        medianIndex += 1
        i += 1
    
    currentIndex = 0    
    GetNextSlidingWindow(listOfMedian, listOfNumber, slidingWindowSize, currentIndex)        
    return listOfMedian

def main():
    arr = [3, 1, 3, 5, 10, 6, 4, 3, 1]    
    print(','.join(map(str, ArrayChallenge(arr))))
    return

main()    