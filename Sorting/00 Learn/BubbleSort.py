class Sort:
    # O(n^2)
    def bubbleSort(self, arr: list[int])->None:
        
        for n in range(len(arr)-1, -1, -1):
            for i in range(0, n):
                if arr[i] > arr[i+1]:
                   arr[i], arr[i+1] = arr[i+1], arr[i]
    


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
    solution.bubbleSort(test['arr'])
    print(test)
    test["arr"] = temp
