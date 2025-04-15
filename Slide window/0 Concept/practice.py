from typing import List
import timeit
# With Brute force
def best_total_price(prices:List[int], k:int)->int:
    maxTotal = 0
    for i in range(len(prices)-k+1):
        total = sum(prices[i:i+k])
        maxTotal = max(maxTotal, total)
    return maxTotal

# With Sliding Window
def best_total_price_sw(prices:List[int], k:int) -> int:
    if len(prices) < k:
        return 0
    maxTotal = sum(prices[:k])
    total = maxTotal
    for i in range(len(prices)-k):
        total -= prices[i]
        total += prices[i+k]
        maxTotal = max(total, maxTotal)
    return maxTotal


prices = [2, 4, 1, 5, 2, 8, 9]
# warm up steps
best_total_price(prices, 3)

start = timeit.timeit()
print(best_total_price(prices, 3))
end = timeit.timeit()
print("Time:", end-start)


start = timeit.timeit()
print(best_total_price_sw(prices, 3))
end = timeit.timeit()
print("Time:", end-start)


