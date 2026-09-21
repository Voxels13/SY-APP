# 0/1 Knapsack using Bottom-Up and Top-Down Dynamic Programming
 
 
# Bottom-Up: fill a table where dp[i][w] = best value using the first i items with capacity w


def knapsack_bottom_up(wt, val, W):
    n = len(wt)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
 
    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]                       # skip item i
            if wt[i - 1] <= w:                            # take item i
                dp[i][w] = max(dp[i][w], val[i - 1] + dp[i - 1][w - wt[i - 1]])
 
    # Backtrack to find which items were picked

    items = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items.append(i)
            w -= wt[i - 1]
 
    return dp[n][W], items[::-1]
 
 
# Top-Down: recursion, with memo to remember answers already computed

def knapsack_top_down(wt, val, W):
    memo = {}
 
    def solve(i, w):
        if i == 0 or w == 0:
            return 0
        if (i, w) not in memo:
            best = solve(i - 1, w)                        # skip item i

            if wt[i - 1] <= w:                            # take item i
                best = max(best, val[i - 1] + solve(i - 1, w - wt[i - 1]))
            memo[(i, w)] = best
        return memo[(i, w)]
 
    return solve(len(wt), W)
 
 
n = int(input("Enter number of items: "))
wt = list(map(int, input("Enter weights: ").split()))
val = list(map(int, input("Enter values: ").split()))
W = int(input("Enter knapsack capacity: "))
 
best, items = knapsack_bottom_up(wt, val, W)
print("\nBottom-Up  max value:", best)
print("Items selected:", items)
print("Top-Down   max value:", knapsack_top_down(wt, val, W))
