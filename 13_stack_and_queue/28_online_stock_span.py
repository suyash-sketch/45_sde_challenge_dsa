class StockSpanner:

    def __init__(self):
        # The stack will store tuples of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # While stack is not empty and the top price is less than or equal to current price
        while self.stack and self.stack[-1][0] <= price:
            # Pop the smaller price and add its span to the current span
            popped_price, popped_span = self.stack.pop()
            span += popped_span
            
        # Push the current price and its accumulated span onto the stack
        self.stack.append((price, span))
        
        return span

# --- Example Execution ---
# spanner = StockSpanner()
# spanner.next(100) -> stack: [(100, 1)], returns 1
# spanner.next(80)  -> stack: [(100, 1), (80, 1)], returns 1
# spanner.next(60)  -> stack: [(100, 1), (80, 1), (60, 1)], returns 1
# spanner.next(70)  -> 70 > 60. Pop 60. span = 1 + 1 = 2. 
#                   -> stack: [(100, 1), (80, 1), (70, 2)], returns 2
# spanner.next(60)  -> stack: [(100, 1), (80, 1), (70, 2), (60, 1)], returns 1
# spanner.next(75)  -> 75 > 60. Pop 60 (span+1). 75 > 70. Pop 70 (span+2). span = 1+1+2 = 4.
#                   -> stack: [(100, 1), (80, 1), (75, 4)], returns 4