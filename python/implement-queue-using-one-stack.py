class MyQueue:

    def __init__(self):
        self.a = []

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        if (len(self.a) == 0):
            return
        x = self.a.pop()
        print("x", x)
        if (len(self.a) == 0):
            return x
        item = self.pop()
        print("item x", item, x)
        self.a.append(x)
        return item

    def peek(self) -> int:
        return self.a[0]

    def empty(self) -> bool:
        return (len(self.a) == 0)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()