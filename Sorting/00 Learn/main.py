class Sorting:
    
    # O(n^2)
    def bubbleSort(self, arr: list[int])->None:
        
        for n in range(len(arr)-1, -1, -1):
            for i in range(0, n):
                if arr[i] > arr[i+1]:
                   arr[i], arr[i+1] = arr[i+1], arr[i]
    

    # O(n^2)
    def selectionSort(self, arr:list[int]) -> None:
        for i in range(len(arr)-1):
            Min = i
            for pivot in range(i+1, len(arr)):
                if arr[pivot] < arr[Min]:
                    Min = pivot

            arr[i], arr[Min] = arr[Min], arr[i]
    
    # O(n^2) Theta(n)
    def insertionSort(self, arr:list[int]) -> None:
        
        for i in range(1, len(arr)):
            j = i-1

            while j >= 0 and arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                j-=1 

    # O(n*logn)
    def mergeSort(self, arr:list[int], s:int, e: int) -> None:
        if e-s+1 <=1:
            return

        m = (s+e)//2
        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m+1, e)

        self.merge(arr, s, m, e)

    def merge(self, arr:list[int], s:int, m:int, e:int):
        
        i = s
        j = m+1
        res = []
        while i<=m and j<=e:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i+=1
            else:
                res.append(arr[j])
                j+=1
        
        while i <= m:
            res.append(arr[i])
            i+=1

        while j <= e:
            res.append(arr[j])
            j+=1

        arr[s:e+1] = res



solution = Sorting()

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
    solution.bubbleSort(**test)
    print(test)
    test["arr"] = temp

    temp = test["arr"].copy()
    solution.selectionSort(**test)
    print(test)
    test["arr"] = temp
    
    temp = test["arr"].copy()
    solution.selectionSort(**test)
    print(test)
    test["arr"] = temp

    temp = test["arr"].copy()
    solution.mergeSort(test['arr'], 0, len(test["arr"])-1)
    print(test)
    test["arr"] = temp