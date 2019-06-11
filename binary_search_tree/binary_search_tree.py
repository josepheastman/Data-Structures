class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif self.value < target:
            if self.right == None:
                return False
            else:
                return BinarySearchTree.contains(self.right, target)
        else:
            if self.left == None:
                return False
            else:
                return BinarySearchTree.contains(self.left, target)

    def get_max(self):
        while self.right:
            self = self.right
        return self.value

    def for_each(self, cb):
        pass
