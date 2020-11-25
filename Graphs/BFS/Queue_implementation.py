class _Node:

    __slots__ = '_element', '_next'

    def __init__(self, element, next):

        self._element = element
        self._next = next


class _Queue:

    __slots__ = '_front', '_rear', '_size'

    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, value):

        node_instance = _Node(value, None)

        if self.is_empty():
            self._front = node_instance
        else:
            self._rear._next = node_instance

        self._rear = node_instance
        self._size += 1

    def dequeue(self):

        if self.is_empty():
            return "Queue is empty"
        else:
            e = self._front._element
            self._front = self._front._next
            self._size -= 1
            if self.is_empty():
                self._rear = None
        return e
