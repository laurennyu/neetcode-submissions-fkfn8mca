class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = [] # minimum of stack as of index i; len should always be >= len of stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.minimum = [val]
        else:
            self.minimum.append(min(val, self.minimum[len(self.stack) - 2]))

    def pop(self) -> None:
        self.minimum.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
