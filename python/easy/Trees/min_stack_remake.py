class minStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val) -> None:
        self.stack.append(val)
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if  self.minStack:
            if self.stack.pop() == self.minStack[-1]:
                self.minStack.pop()

        return

    def getMin(self) -> int:
        if not self.minStack:
            return None
        return self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]