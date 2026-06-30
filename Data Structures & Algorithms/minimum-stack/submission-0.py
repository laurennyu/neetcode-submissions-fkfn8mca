class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = [] # minimum of stack as of index i; len should always be >= len of stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.minimum = [val]
        else:
            curr_min = min(val, self.minimum[len(self.stack) - 2])
            if len(self.minimum) < len(self.stack):
                self.minimum.append(curr_min)
            else:
                self.minimum[len(self.stack) - 1] = curr_min

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[len(self.stack) - 1]
