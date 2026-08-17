class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if not self.stk or val < self.stk[-1][1]:
            self.stk.append((val, val))
        else:
            self.stk.append((val, self.stk[-1][1]))

    def pop(self) -> None:
        return self.stk.pop()        

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]
