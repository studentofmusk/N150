class Sort:
    def quickSort(self, arr: list[int], start: int, end: int):

        if (end-start+1) <= 1:
            return
        
        pivot = arr[end]
        left = start

        for i in range(start, end):
            if arr[i] < pivot:
                arr[i], arr[left] = arr[left], arr[i]
                left +=1
        
        arr[left], arr[end] = arr[end], arr[left]

        self.quickSort(arr, start, left-1)        
        self.quickSort(arr, left+1, end)


solution = Sort()

test_cases = [
    # 1. Already sorted array
    {"arr": [1, 2, 3, 4, 5, 6, 7]},  

    # 2. Reverse sorted array
    {"arr": [9, 8, 7, 6, 5, 4, 3]},  

    # 3. Array with duplicates
    {"arr": [8, 3, 4, 61, 3, 5, 5]},  

    # 4. Array with negative numbers
    {"arr": [-5, -1, -10, 0, 7, 2, -3]},  

    # 5. Single element + mix of large numbers
    {"arr": [1000000, 999999, 123456, 1, 500, 999999, 42]}  
]

for test in test_cases:
    solution.quickSort(test["arr"], 0, len(test["arr"])-1)
    print(test)