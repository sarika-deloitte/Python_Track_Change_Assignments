# 4. Write a decorator to cache function invocation results. Store pairs arg:result in a dictionary in an attribute of the function object. The function being memoized is:
# def fibonacci(n):
# assert n >= 0
# if n < 2:
# return n
# else:
# return fibonacci(n-1) + fibonacci(n-2)

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

@memoize
def fibonacci(n):
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# Example usage
print(fibonacci(10))  # Output: 55
print(fibonacci.cache)  # Output: {(0,): 0, (1,): 1, (2,): 1, (3,): 2, (4,): 3, (5,): 5, (6,): 8, (7,): 13, (8,): 21, (9,): 34, (10,): 55}

