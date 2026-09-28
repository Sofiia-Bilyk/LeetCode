from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        if amount < coins[0]:
            return -1

        arr = [-1] * (amount + 1)

        arr[0], arr[coins[0]] = 0, 1
        i = coins[0] + 1
        while i <= amount:
            for coin in coins:
                if coin > i:
                    break
                elif arr[i-coin] == -1:
                    pass
                elif arr[i] == -1:
                    arr[i] = arr[i-coin] + 1
                else:
                    arr[i] = min(arr[i], arr[i-coin] + 1)
            i += 1
        return arr[amount]
