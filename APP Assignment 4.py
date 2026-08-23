#Iterative (Tabulation)

def fibonacci(n):

    if n == 0:
        return 0

    if n <= 1:
        return n

    #Array to store calculated values

    dp = [0] * (n+1)

    #Base Cases

    dp[0] = 0

    dp[1] = 1


    #Calculation (Iteration part)

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

if __name__ == "__main__":

    n = int(input("Enter nth Fibonacci number: "))
    result = fibonacci(n)

    print(f"{n}th Fibonacci number: {result}")



#Recursive (Memoization)

def fibonacci(n,memo):

    #Base case for loop

    if n <= 1:
        return n


    if memo[n] != -1:
        return memo[n]


    #Recursion part

    memo[n] = fibonacci(n-1,memo) + fibonacci(n-2,memo)

    return memo[n]


def dp_table(n):

    memo = [-1] * (n+1)     #Here , we use -1 instead of 0 to tell the interpreter that we are storing yet to be calculated (uncalculated) values

    return fibonacci(n,memo)
        


if __name__ == "__main__":

    n = int(input("Enter nth fibonacci number: "))
    result = dp_table(n)

    print(f"{n}th fibonacci number: {result}")



#Iterative
#No arrays (Saves memory)


def fibonacci(n):

    if n <= 1:
        return n

    #Variable to store current fibonacci number

    curr = 0

    #Variables to perform addition upto nth addition number

    prev1 = 0
    prev2 = 1

    for i in range(2,n+1):
        curr = prev1 + prev2

        prev1 = prev2
        prev2 = curr

    return curr


if __name__ == "__main__":

    n = int(input("Enter nth fibonacci number: "))
    result = fibonacci(n)

    print(f"{n}'th fibonacci number: {result}")



#Iterative with Dictionaries (Saves on lookup time {0(1)})

def fibonacci(n):

    memo = {}

    #Base Case

    memo[0] = 0
    memo[1] = 1

    #Iterative process

    for i in range(2,n+1):

        if n <=1:
                return 1

        else:

            memo[i] = memo[i-1] + memo[i-2]


    return memo[n]


if __name__ == "__main__":

    n = int(input("Enter nth fibonacci number: "))
    result = fibonacci(n)

    print(f"{n}th fibonacci value: {result}")



#Recursive with Dictionaries (Saves lookup time {0(1)})

memo = {}

def fibonacci(n):

    if n in memo:
        return memo[n]

    if n<= 1:
        return n

    elif n == 2:
        return 1

    else:

        result = fibonacci(n-1) + fibonacci(n-2)

    memo[n] = result

    return memo[n]



if __name__ == "__main__":

    n = int(input("Enter nth fibonacci number: "))
    result = fibonacci(n)

    print(f"{n}th fibonacci value = {result}")

    