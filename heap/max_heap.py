class Heap:
    def __init__(self):
        self.storage = [0]

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if len(self.storage) > 2:
            self.__swap(1, len(self.storage) - 1)
            max = self.storage.pop()
            self._sift_down(1)
        elif len(self.storage) == 2:
            max = self.storage.pop()
        else:
            max = False
        return max

    def get_max(self, index):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def __swap(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

    def _bubble_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.storage[index] > self.storage[parent]:
            self.storage[index]
            self.storage[parent]
        self._bubble_up(parent)

    def _sift_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.storage) > left and self.storage[largest] < self.storage[left]:
            largest = left
        if len(self.storage) > right and self.storage[largest] < self.storage[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self._sift_down(largest)
