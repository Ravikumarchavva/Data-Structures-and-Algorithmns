class Fibonacci:
    def fib(self, num: int) -> int:
        prev_1, prev_2 = 0, 1

        for _ in range(2, num+1):
            curr = prev_1 + prev_2
            prev_1, prev_2 = prev_2, curr

        return curr
    
if __name__ == "__main__":
    fib = Fibonacci()
    print(fib.fib(5))  # Output: 5
    print(fib.fib(10)) # Output: 55