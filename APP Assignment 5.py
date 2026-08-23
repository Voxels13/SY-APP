def lcs(X,Y):
    m,n = len(X), len(Y)
    dp = [[0] * (n+1) for _ in range (m+1)] #This makes a table with Rows of X and Columns of Y  e.g: for m (No of rows) = 3 and n (no of columns (elements) = 3 [ [0,0,0], [0,0,0] , [0,0,0]]
    #Here, we do (n+1) and (m+1) for the base case of the entire table , i.e , a column with only 0's

    for i in range (1,m+1):

        for j in range(1,n+1):

            if X[i-1] == Y[j-1]:  #Checking for if A == B , for each value of X , we check every value of Y

                dp[i][j] = dp[i-1][j-1] + 1 #if a match occurs, increment the previous value in the table by 1

            else:

                dp[i][j] = max(dp[i-1][j],dp[i][j-1]) #If a match does not occur, retain the maximum / current value (ensures that the last increment dosent disappear and is instead retained)  --> compares the value above or behind the current pointer and retains the max value from either one

    return dp[m][n]

print(lcs("ABCBDAB","BDCABA"))