# 求立方根
def cube_root(number, accuracy):
    """ 求立法根函数

    Args:
        number (int): 要求立法根的数
        accuracy (int): 精确度，输入1表示精确到 0.0000001
    """
    bottom_bound = 1
    upper_bound = number ** 0.5
    # step = repr(accuracy)
    btime = utime = 0
    while True:
        possible_value = (upper_bound + bottom_bound) / 2
        temp_value = number - possible_value ** 3
        if abs(temp_value) <= accuracy/1000000:
            print("The cube root is:", possible_value)
            break
        elif temp_value > 0:
            bottom_bound = (upper_bound + bottom_bound) / 2
            btime += 1
            print("bottom rise time:", btime, bottom_bound)
        elif temp_value < 0:
            upper_bound = (upper_bound + bottom_bound) / 2
            utime += 1
            print("upper decrease time:", utime, upper_bound)

# number = float(input("Please input the number you want to get its cube root: >"))
# accuracy = float(input("please input the accuracy you want: >"))
# cube_root(number,accuracy)


# 求平方根
def square_root(numb, acc):
    """求平方根函数

    Args:
        numb (int): 要求的数
        acc (int): 精确度

    Raises:
        ZeroDivisionError: 输入负数则抛出此异常

    Returns:
        float: 所求的平方根值
    """
    if numb < 0:
        raise ZeroDivisionError

    def tmp_root(bottom, upper):
        while True:
            root = (upper+bottom)/2
            print(bottom, upper)
            if abs(root*root-numb) <= acc/1000000:
                return root
            elif root*root > numb:
                upper = root
            else:
                bottom = root

    if numb > 1:
        bottom, upper = 0, numb
        return tmp_root(bottom, upper)
    elif numb < 1:
        bottom, upper = numb, 1
        return tmp_root(bottom, upper)
    else:
        return 1


# 求平方根. advanced
def sqrt(number, accuracy):
    """牛顿法求平方根，效率提高

    Args:
        number (int): 要求的数
        accuracy (int): 精确度

    Returns:
        float: 求得的值
    """
    root = 1
    while True:
        temp = root
        root -= (root*root-number)/(2*root)
        print(root, temp)
        if abs(temp-root) <= accuracy/1000000:
            return root


print(square_root(0.88888888, 10))
print()
print(sqrt(0.88888888, 10))
