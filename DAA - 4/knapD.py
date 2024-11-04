def knapsack(weights, values, capacity):
    n =len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n+1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w :
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    max_value = dp[n][capacity]
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]

    selected_items.reverse()

    return max_value, selected_items

weights = [10,20,30]
values = [60,100,120]
capacity = 50

max_value, selected_items = knapsack(weights, values, capacity)
print(f"Maximum value: {max_value}")
print(f"Selected items: {selected_items}")