number = float(input("Please input the number you want to get its cube root: >"))
accuracy = float(input("please input the accuracy you want: >"))
bottom_bound = 1
upper_bound = number ** 0.5
step = repr(accuracy)
btime = utime = 0
while True:
    possible_value = (upper_bound + bottom_bound) / 2
    temp_value = number - possible_value ** 3
    if abs(temp_value) <= accuracy/1000:
        print("The cube root is:", possible_value)
        break
    elif temp_value > 0:
        bottom_bound = (upper_bound + bottom_bound) / 2
        btime += 1
        print("bottom rise time:",btime,bottom_bound)
    elif temp_value < 0:
        upper_bound = (upper_bound + bottom_bound) / 2
        utime += 1
        print("upper decrease time:", utime,upper_bound)