# 0x08 - Making Change

##  Greedy Algorithms

Greedy algorithms are used to solve optimization problems by making the locally optimal choice at each step. In the context of the coin change problem, a greedy algorithm would choose the largest coin denomination that fits into the remaining amount at each step. Greedy algorithms are suitable for the coin change problem because they provide a quick solution and are easy to implement. However, they might not always produce the optimal solution, especially if the coin denominations are not well-suited for the problem or if the problem has constraints that cannot be satisfied by a greedy approach.

```
def make_change_greedy(coins, amount):
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        num_coins += amount // coin
        amount %= coin
    return num_coins
```

##  Dynamic Programming

Dynamic programming is a method used to solve optimization problems by breaking them down into simpler sub-problems and solving each sub-problem only once, storing the solution to each sub-problem to avoid redundant computations. In the context of the coin change problem, dynamic programming is highly effective because it allows us to efficiently compute the minimum number of coins required to make change for any amount. Key concepts in dynamic programming include identifying overlapping subproblems and optimal substructure, which enable us to apply memoization or bottom-up tabulation to solve the problem efficiently.

```
def make_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

##  Algorithmic Complexity

Analyzing the time and space complexity of algorithms is essential for understanding their performance characteristics and ensuring that they meet runtime constraints. For the making change problem, we strive to find solutions with lower time complexity to handle larger inputs efficiently. Dynamic programming solutions typically have polynomial time complexity, making them suitable for solving the making change problem efficiently even for large amounts.


## Problem-Solving Strategies

Problem-solving strategies involve breaking down complex problems into smaller, manageable sub-problems, which can be solved individually and then combined to solve the original problem. Iterative and recursive approaches are common strategies used in dynamic programming. Iterative approaches involve solving sub-problems in a bottom-up manner, starting from the smallest sub-problems and gradually building up to the larger problem. Recursive approaches, on the other hand, involve solving the larger problem by recursively solving smaller sub-problems. Both approaches have their advantages and disadvantages, and the choice between them depends on the problem constraints and personal preference.


##  Python Programming

Python programming skills are essential for implementing solutions to the making change problem. This includes manipulating lists and using list comprehensions to generate lists efficiently. Implementing functions with efficient looping and conditional statements is also crucial for writing clean and optimized code. Python's built-in data structures and libraries provide powerful tools for solving algorithmic problems, making it a popular choice for implementing dynamic programming solutions to the making change problem.