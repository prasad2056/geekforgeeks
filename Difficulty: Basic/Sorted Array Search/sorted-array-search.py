#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code her
        return 1 if K in arr else -1
        
        sol = Solution()
        
        # Test case
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        K = 5
        print(sol.searchInSorted(arr, K))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        NK = input().strip().split()
        N = int(NK[0])
        K = int(NK[1])
        A = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.searchInSorted(A, N, K))

# } Driver Code Ends