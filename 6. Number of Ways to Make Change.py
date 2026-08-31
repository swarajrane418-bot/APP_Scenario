coins = list(map(int, input("Enter coin denominatons: ").split()))

amount = int(input("Enter target amount:"))


dp = [0] * (amount + 1)

dp[0] = 1


for coin in coins:
    for i in range(coin, amount + 1):
        dp[i] += dp[i - coin]


print("Total number of combinations:", dp[amount])
