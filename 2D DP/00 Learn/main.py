# Brute Force - Time and Space: O(2^(n+m))
def bruteForce(r, c, rows, cols):
    if r == rows or c == cols:
        return 0
    if r == rows-1 and c == cols-1:
        return 1
    return (
        bruteForce(r+1, c, rows, cols) +
        bruteForce(r, c+1, rows, cols)
    )

# print(bruteForce(0, 0, 100, 100))

# Memorization - Time and Space: O(n*m)
def memorization(r, c, rows, cols, cache):
    if r == rows or c == cols:
        return 0
    if cache[r][c] > 0:
        return cache[r][c]
    if r == rows - 1 and c == cols - 1:
        return 1

    cache[r][c] = (
        memorization(r+1, c, rows, cols, cache) +
        memorization(r, c+1, rows, cols, cache)
    )

    return cache[r][c]


print(memorization(0, 0, 100, 100, [[0]*100 for i in range(100)]))


def dp(rows, cols):
    prevRow = [0] * cols

    for r in range(rows-1, -1, -1):
        curRow = [0] * cols
        curRow[cols-1] = 1
        for c in range(cols-2, -1, -1):
            curRow[c] = curRow[c+1] + prevRow[c]
        prevRow = curRow
    return prevRow[0]


print(dp(100, 100))