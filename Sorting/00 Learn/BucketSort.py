class Sort:
    def bucketSort(self, arr:list[int])->list[int]:
        if not arr:
            return []
        
        small, large = min(arr), max(arr)
        cache = [0] * (large - small + 1)

        # fill counts
        for num in arr:
            cache[num - small] += 1

        # rebuild sorted result
        res = []
        for idx, count in enumerate(cache):
            res.extend([idx + small] * count)
        
        return res



solution = Sort()

test_cases = [
    {"arr": [1, 2, 3, 4, 5, 6, 7]},   # sorted
    {"arr": [9, 8, 7, 6, 5, 4, 3]},   # reverse
    {"arr": [8, 3, 4, 61, 3, 5, 5]},  # duplicates
    {"arr": []},                      # empty
    {"arr": [-3, -1, -2, 0, 2, 1]},   # negatives
]


for test in test_cases:
    print(solution.bucketSort(**test))