from linkedlist import LinkedList


class Queue:
    def __init__(self, head=None):
        self.size = 0
        # What data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            return self.storage.delete_from_head()

    def len(self):
        return self.size
