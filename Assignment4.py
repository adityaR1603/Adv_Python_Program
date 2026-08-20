# Memoization
def fibonacci_memo(n, memo):
    if n <= 1:
        return n
        
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Tabulation
def fibonacci_tabulation(n):
    if n <= 1:
        return n
    fibonacci = [0] * (n + 1)
    fibonacci[0] = 0
    fibonacci[1] = 1
    for i in range(2, n + 1):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
    return fibonacci[n]

# Main program

n = int(input("Enter n: "))
# Memoization
memo = {}
answer1 = fibonacci_memo(n, memo)

# Tabulation
answer2 = fibonacci_tabulation(n)
print("Using Memoization:", answer1)
print("Using Tabulation:", answer2)
