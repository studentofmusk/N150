# Min Heap
class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)

        i = len(self.heap)-1
        while i > 1 and self.heap[i] < self.heap[i//2]:
            temp = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = temp
            i = i//2


    def pop(self):
        if len(self.heap) == 1:
            return None
        elif len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]

        # Move last value to top
        self.heap[1] = self.heap.pop()
        # Percolate Down
        i = 1
        while i * 2 < len(self.heap):
            if (
                i*2+1 < len(self.heap) and
                self.heap[2 * i +1] < self.heap[2 * 1] and
                self.heap[i] > self.heap[2 * i + 1]
            ):
                # Swap right child
                temp = self.heap[i]
                self.heap[i] = self.heap[2*i+1]
                self.heap[2 * i + 1] = temp
                i = 2 * i + 1
            elif self.heap[2 * i] < self.heap[i]:
                # Swap left child
                temp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = temp
                i = 2 * i
            else:
                break
        return res

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def heapify(self, arr):
        # 0-th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1)//2

        while cur > 0:
            # Percolate down
            i = cur

            while 2 * i < len(self.heap):
                if (
                        2 * i + 1 < len(self.heap) and
                        self.heap[2 * i + 1] < self.heap[2 * i] and
                        self.heap[i] > self.heap[2 * i + 1]
                ):
                    # Swap right chile
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = temp
                    i = 2 * i + 1

                elif self.heap[2 * i] < self.heap[i]:
                    # Swap left child
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = temp
                    i = 2 * i
                else:
                    break
            cur -= 1
minHeap = Heap()
minHeap.push(3)
minHeap.push(56)
minHeap.push(32)
minHeap.push(1)
print(minHeap.pop())