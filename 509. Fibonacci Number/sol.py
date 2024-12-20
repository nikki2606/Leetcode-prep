class Solution:
    def fib(self, n: int) -> int:
        # Memoization
        def fibo(n, memo):
            if memo[n]:
                return memo[n]

            if n == 0 or n == 1:
                return n
            
            res = fibo(n-1, memo) + fibo(n-2, memo)
            memo[n] = res
            return res
        
        memo = [0]*(n+1)
        return fibo(n, memo)