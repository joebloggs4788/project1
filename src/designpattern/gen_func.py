def gen_squares(n):
    i = 0
    while i < n:
        yield i*i
        print(f"i is {i}")
        i += 1

if __name__ == "__main__":
    g = gen_squares(4)
    print(g.__next__())
    print("-----------")
    print(g.__next__())
    print("-----------")
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())