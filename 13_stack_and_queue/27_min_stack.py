class MinStack:
    def __init__(self):
        # Initialize a stack
        self.st = []
        # To store the minimum value
        self.mini = None

    # Method to push a value in stack
    def push(self, value):
        # If stack is empty
        if not self.st:
            # Update the minimum value
            self.mini = value

            # Push current value as minimum
            self.st.append(value)
            return

        # If the value is greater than the minimum
        if value > self.mini:
            self.st.append(value)
        else:
            # Add the modified value to stack
            self.st.append(2 * value - self.mini)
            # Update the minimum
            self.mini = value

    # Method to pop a value from stack
    def pop(self):
        # Base case
        if not self.st:
            return

        # Get the top
        x = self.st.pop()

        # If the modified value was added to stack
        if x < self.mini:
            # Update the minimum
            self.mini = 2 * self.mini - x

    # Method to get the top of stack
    def top(self):
        # Base case
        if not self.st:
            return -1

        # Get the top
        x = self.st[-1]

        # Return top if minimum is less than the top
        if self.mini < x:
            return x

        # Otherwise return mini
        return self.mini

    # Method to get the minimum in stack
    def getMin(self):
        # Return the minimum
        return self.mini


if __name__ == "__main__":
    s = MinStack()

    # Function calls
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin(), end=" ")
    s.pop()
    print(s.top(), end=" ")
    s.pop()
    print(s.getMin())