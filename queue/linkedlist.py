class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_to_head(self, value):
        new_head = Node(value)
        new_head.set_next(self.head)

        if (self.head == None):
            self.tail = new_head
            self.head = new_head

    def add_to_tail(self, value):
        new_tail = Node(value)
        if self.head == None:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.set_next(new_tail)
            self.tail = new_tail
        return self

    def delete_from_head(self):
        if self.head is not None:
            previous = self.head.value
            self.head = self.head.get_next()

            if self.head == None:
                self.tail = None

            return previous
