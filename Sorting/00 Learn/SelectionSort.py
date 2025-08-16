class Sort:
    # O(n^2)
    def selectionSort(self, arr:list[int]) -> None:
        for i in range(len(arr)-1):
            Min = i
            for pivot in range(i+1, len(arr)):
                if arr[pivot] < arr[Min]:
                    Min = pivot

            arr[i], arr[Min] = arr[Min], arr[i]
    




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
    
    temp = test["arr"].copy()
    solution.selectionSort(**test)
    print(test)
    test["arr"] = temp
