def main(func, *args):
    print(func(args))

def func(n):
    return n

main(func,10)