
def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f"hello {name}"



print(greet("faizan"))


print()

def even(n):
    for x in range(2, n+1, 2):
        yield x


for y in even(n = 10):
    print(y)

