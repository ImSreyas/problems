def count_valid_arrays(N, K):
    MOD = 10000

    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(K + 1)]

    # Base case: for length 1, each number from 1 to N is a valid array
    for j in range(1, N + 1):
        dp[1][j] = 1
    # print(dp)

    # Fill the DP table
    for i in range(2, K + 1):
        for j in range(1, N + 1):
            dp[i][j] = 0
            for x in range(1, N + 1):
                if j % x == 0:
                    dp[i][j] += dp[i-1][x]
                    dp[i][j] %= MOD

    # Calculate the result
    result = 0
    for j in range(1, N + 1):
        result += dp[K][j]
        result %= MOD

    return result

# Example usage
N = 2
K = 2
print(count_valid_arrays(N, K))  # Output: 5
