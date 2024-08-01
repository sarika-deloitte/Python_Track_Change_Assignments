# 5. Write a timer decorator to find the speedup due to the memorization in question 4

import time

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    wrapper.cache = cache
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@memoize
@timer
def fibonacci(n):
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
if __name__ == "__main__":
    print(fibonacci(10))  # Output: 55 and the time taken
    print(fibonacci.cache)  # Output: {(0,): 0, (1,): 1, (2,): 1, (3,): 2, (4,): 3, (5,): 5, (6,): 8, (7,): 13, (8,): 21, (9,): 34, (10,): 55}
