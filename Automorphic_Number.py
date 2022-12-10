def isAutomorphic(N) :
 
    # Store the square
    sq = N * N
      
    # Start Comparing digits
    while (N > 0) :
 
        # Return false, if any digit of N doesn't
        # match with its square's digits from last
        if (N % 10 != sq % 10) :
            return False
   
        # Reduce N and square
        N //= 10
        sq //= 10
   
    return True
   
# Driver code
N=int(input())
if isAutomorphic(N) :
    print ("Automorphic Number")
else :
    print  ("Not an Automorphic Number")