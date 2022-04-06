class MyStack:

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        if (len(self.a) == 0):
            return
        self.b = []
        for i in range(len(self.a) - 1, -1, -1):
            self.b.append(self.a[i])
        x = self.b.pop(0)
        self.a = []
        # print(self.b)
        for i in range(len(self.b) - 1, -1, -1):
            self.a.append(self.b[i])
        # print("a",self.a)
        return x

    def top(self) -> int:
        return self.a[-1]

    def empty(self) -> bool:
        # print(self.a)
        return (len(self.a) == 0)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()