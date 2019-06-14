class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        pass

    def get_max(self, index):
        maxEl = self.storage[index // 2]
        for i in range(1 + index // 2, index):
            maxEl = max(maxEl, self.storage[i])
        return maxEl

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.storage[index] > self.storage[parent]:
            self.storage(index, parent)
            self.storage(parent)
        self._bubble_up(parent)

    def _sift_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.sift_down(largest)
