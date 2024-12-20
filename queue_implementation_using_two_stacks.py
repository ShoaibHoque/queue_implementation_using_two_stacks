class Stack:
    def __init__(self):
        self.container = []

    def push(self, value: int) -> None:
        self.container.append(value)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.container.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.container[-1]

    def is_empty(self) -> bool:
        return len(self.container) == 0

    def size(self) -> int:
        return len(self.container)

class Queue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self, x: int) -> None:
        self.stack_in.push(x)

    def dequeue(self) -> int:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        if self.stack_out.is_empty():
            raise IndexError("Queue is empty")
        return self.stack_out.pop()

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
q.enqueue(3)
print(q.dequeue())  # Output: 2
