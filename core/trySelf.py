# 斐波那契数列
def fibonacci(num: int):
    """求斐波那契数列

    Args:
        num (int): 求数列的前多少位

    Returns:
        list: 斐波那契数列
    """
    back1, back2 = 0, 1
    fibo = [back1, back2]
    for i in range(num-2):
        back1, back2 = back2, back2+back1
        fibo.append(back2)
    if num < 2:
        fibo = fibo[:1]
    return fibo


# 闭包函数 求 斐波那契数列
def closure_fibo():
    """求斐波那契数列

    Returns:
        int: 斐波那契数列中的某一位的值
    """
    b1, b2 = 0, 1

    def next():
        nonlocal b1, b2
        temp = b1
        b1, b2 = b2, b2+b1
        return temp
    return next


# print(fibonacci(int(input())))

f1 = fibonacci
print(f1(10))

f2 = closure_fibo()
for i in range(10):
    print(f2())
