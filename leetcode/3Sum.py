from collections import Counter

def speedup(numbers):
    result = [[0, 0, 0]] if numbers.count(0) > 2 else []
    ocur_numbers = Counter(numbers)
    twice_numbers = [x for x, y in ocur_numbers.items() if y > 1]
    ordered_numbers = sorted(ocur_numbers.keys())
    ordered_dict = dict()
    for index, val in enumerate(ordered_numbers):
        ordered_dict[val] = index
    ordered_count = len(ordered_numbers)
    running_times = 0
    for outer in range(ordered_count - 1):
        used_number = set()
        for inter in range(outer + 1, ordered_count):
            need = - (ordered_numbers[outer] + ordered_numbers[inter])
            running_times += 1
            if need in ordered_dict:
                index = ordered_dict[need]
                if index > outer and index != inter:
                    if inter in used_number or index in used_number:
                        break
                    else:
                        used_number.add(inter)
                        used_number.add(index)
                        result.append([ordered_numbers[outer], ordered_numbers[inter], need])

    for match_twice in twice_numbers:
        need = -2 * match_twice
        running_times += 1
        if need in ordered_numbers and need != 0:
            result.append([need, match_twice, match_twice])
    print("running Times", running_times)
    return result