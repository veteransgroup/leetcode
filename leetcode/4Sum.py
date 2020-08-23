from collections import Counter

def fourSum(numbers, target):
    result = set()
    counter = Counter(numbers)
    twice_numbers = [x for x, y in counter.items() if y == 2]
    third_numbers = [x for x, y in counter.items() if y == 3]
    fourth_numbers = [x for x, y in counter.items() if y > 3]
    multi_numbers = twice_numbers + third_numbers + fourth_numbers
    ordered_numbers = sorted(counter.keys())
    ordered_count = len(ordered_numbers)
    ordered_dict = dict()
    multi_dict = dict()
    for index, val in enumerate(ordered_numbers):
        ordered_dict[val] = index
    for index, val in enumerate(multi_numbers):
        multi_dict[val] = index
    running_times = 0
    for first in range(ordered_count - 2):
        for second in range(first + 1, ordered_count - 1):
            used_numbers = set()
            for third in range(second + 1, ordered_count):
                need = target - (ordered_numbers[first] + ordered_numbers[second] + ordered_numbers[third])
                running_times += 1
                if need in ordered_dict:
                    index = ordered_dict[need]
                    if index in (first,second,third):
                        if not need in multi_dict:
                            continue
                    if need in used_numbers or ordered_numbers[third] in used_numbers:
                        continue
                    else:
                        used_numbers.add(need)
                        used_numbers.add(ordered_numbers[third])
                        result.add(
                            tuple(sorted([ordered_numbers[first], ordered_numbers[second], ordered_numbers[third], need])))


    for f_times in fourth_numbers:
        if f_times * 4 == target:
            result.add(tuple(sorted([f_times, f_times, f_times, f_times])))
            break
    for three_times in third_numbers + fourth_numbers:
        need = target - three_times * 3
        if need in ordered_dict and need != three_times:
            result.add(tuple(sorted([three_times, three_times, three_times, need])))
            break
    used_multi_numbers = set()
    for two_times in multi_dict:
        if (target - two_times * 2) % 2 == 0:
            need = (target - two_times * 2) / 2
            if need in multi_dict and need != two_times:
                if need in used_multi_numbers or two_times in used_multi_numbers:
                    pass
                else:
                    used_multi_numbers.add(need)
                    used_multi_numbers.add(two_times)
                    result.add(tuple(sorted([need, need, two_times, two_times])))

    return result


lst = [0, 0, 0, 0]
lst_1 = [1, 0, -1, 0, -2, 2]
lst_2 = [-4, 0, -4, 2, 2, 2, -2, -2]
lst_3 = [0, 2, 2, 2, 10, -3, -9, 2, -10, -4, -9, -2, 2, 8, 7]
lst_4 = [-6, 6, -5, 1, -2, -7, -3, -6, 3, -2, 10, 6, 9, 0, -10, 5, 8, 4, -6]
lst_5 = [-3,-2,-1,0,0,1,2,3]

print(fourSum(lst_5, 0))
