from collections import deque


class DonotMatchException(Exception):
    def __init__(self, msg):
        self.message = "Do not match, the issue is %s" % msg
        super().__init__(self.message)


class Solution:

    @staticmethod
    def parse_pattern(pattern):
        simplest_patterns = deque()
        concise_patterns = deque()
        min_length_string = 0
        dot_asterisk = dict()
        pts = pattern.split('*')
        if len(pts) == 1:
            simplest_patterns.appendleft(pattern)
            concise_patterns.appendleft(pattern)
            min_length_string = len(pattern)
            return simplest_patterns, concise_patterns, dot_asterisk, min_length_string

        # last_char_is_asterisk = True if pts[len(pts) - 1] == '' else False
        pat = [p + '*' for p in pts]
        if not pts[len(pts) - 1]:
            pat.pop()
        else:
            pat[len(pat) - 1] = pat[len(pat) - 1][:-1]
        for micro_pattern in pat:
            if micro_pattern.endswith('*') and len(micro_pattern) > 2:
                simplest_patterns.appendleft(micro_pattern[:-2])
                simplest_patterns.appendleft(micro_pattern[-2:])
            else:
                simplest_patterns.appendleft(micro_pattern)
        asterrisk_counter = should_del = clearance = 0
        while len(simplest_patterns):
            tiny_pattern = simplest_patterns.pop()
            skip_nums = 0
            if len(tiny_pattern) == 1:
                skip_nums += simplest_patterns.count('.')
            elif len(tiny_pattern) == 2:
                skip_nums += simplest_patterns.count('..')
            elif len(tiny_pattern) == 3:
                skip_nums += simplest_patterns.count('...')
            if tiny_pattern.endswith('*'):
                if len(concise_patterns) == 0 or tiny_pattern != concise_patterns[0]:
                    asterrisk_counter += 1
                    concise_patterns.appendleft(tiny_pattern)
                    if tiny_pattern == '.*':
                        should_del += 1
                        clearance += 1
            else:
                min_length_string += len(tiny_pattern)
                if asterrisk_counter and should_del:
                    for _ in range(asterrisk_counter):
                        concise_patterns.popleft()
                    concise_patterns.appendleft(".*")
                    dot_asterisk[(tiny_pattern, skip_nums + simplest_patterns.count(tiny_pattern))] = min_length_string
                asterrisk_counter = should_del = 0
                concise_patterns.appendleft(tiny_pattern)
        if asterrisk_counter and should_del:
            for d in range(asterrisk_counter):
                concise_patterns.popleft()
            concise_patterns.appendleft(".*")
            if not tiny_pattern.endswith('*'):
                min_length_string += len(tiny_pattern)
                concise_patterns.appendleft(tiny_pattern)
                dot_asterisk[(tiny_pattern, skip_nums + simplest_patterns.count(tiny_pattern))] = min_length_string
            else:
                dot_asterisk[(tiny_pattern, skip_nums + simplest_patterns.count(tiny_pattern))] = min_length_string
                ##############################

        for index in range(len(concise_patterns) - 1, -1, -1):
            simp_pattern = concise_patterns[index]
            if clearance and simp_pattern.endswith('*') and simp_pattern[0] != '.':
                continue
            simplest_patterns.appendleft(simp_pattern)
        return simplest_patterns, concise_patterns, dot_asterisk, min_length_string

    @staticmethod
    def find_in_string(string, pattern, compare=False):
        if compare:
            if len(string) != len(pattern):
                return False
            for s, p in zip(string, pattern):
                if s != p and p != '.':
                    return False
            return True
            # raise DonotMatchException(string+" vs "+pattern)
        else:
            found = dict()
            len_pattern = len(pattern)
            for index in range(len(string) - len_pattern + 1):
                substr = string[index:index + len_pattern]
                if Solution.find_in_string(substr, pattern, True):
                    found[index] = substr
            return found

    @staticmethod
    def has_done(patterns, remains=False):
        at_least_char_numbers = 0
        for index in range(len(patterns) - 1, -1, -1):
            _pattern = patterns[index]
            if remains:
                if not _pattern.endswith('*'):
                    at_least_char_numbers += len(_pattern)
            else:
                if not (len(_pattern) == 2 and _pattern[1] == '*'):
                    return False
        return at_least_char_numbers if remains else True

    @staticmethod
    def isPass(string, patterns, dots, min_len):
        len_string = len(string)
        if len_string < min_len:
            return False
        print("patterns:", patterns)
        print("dot asterisk:", dots)
        print("Min string chars:", min_len)
        start = 0
        asterisk_no = 0
        while len(patterns):
            current_pattern = patterns.pop()
            if not current_pattern.endswith('*'):
                if Solution.find_in_string(string[start:start + len(current_pattern)], current_pattern, True):
                    start += len(current_pattern)
                else:
                    return False
            else:
                head = current_pattern[0]
                if head != '.':  # 星号后不可能遇到.* 可能遇到a-z*但不会是自己 或 .. 或普通字符
                    moved_steps = 0
                    try:
                        while string[start] == head:
                            start += 1
                            moved_steps += 1
                    except IndexError:
                        if Solution.has_done(patterns):
                            return True
                    if moved_steps:
                        target_head = string[start] if start < len_string else False
                        next_pattern = False
                        while len(patterns):
                            next_pattern = patterns[len(patterns) - 1]
                            if next_pattern.endswith('*') and next_pattern[0] != target_head:
                                if target_head:
                                    if next_pattern[0] != target_head:
                                        patterns.pop()
                                else:
                                    patterns.pop()
                            else:
                                break
                        if next_pattern:
                            if next_pattern in ('.', '..', '...', '....', '.....') and target_head:
                                moved_steps = len(next_pattern) - (len_string - start)
                            for next_head in next_pattern:  # solve input = aaa, a*aa
                                if moved_steps > 0:
                                    if next_head == head:
                                        moved_steps -= 1
                                        start -= 1
                                    elif next_head == '.':
                                        moved_steps -= 1
                                        start -= 1
                else:
                    if Solution.has_done(patterns):
                        return True
                    next_pattern, remain_numbers = list(dots.keys())[asterisk_no]
                    found_next = list(Solution.find_in_string(string[start:], next_pattern).keys())
                    if len(found_next):
                        if patterns.count(".*") > 0:
                            start += found_next[0]
                        else:
                            start += found_next[len(found_next) - remain_numbers - 1]
                    else:
                        return False
                    if next_pattern in ('.', '..', '...'):
                        remain_chars_for_dots = Solution.has_done(patterns, True)  # 计算剩下多少点
                        if remain_chars_for_dots > len_string - start:
                            start -= remain_chars_for_dots - (len_string - start)
                    asterisk_no += 1

        if start == len_string:
            return True
        else:
            return False

    @staticmethod
    def isMatch(string, pattern_in):
        simplested, patterns, dots, min_len = Solution.parse_pattern(pattern_in)
        if Solution.isPass(string, patterns, dots, min_len):
            return True
        else:
            return Solution.isPass(string, simplested, dots, min_len)


# print(Solution.isMatch(
# "mississippi",
# "mis*is*ip*."))
#
# print(Solution.isMatch(
# "bbcacbabbcbaaccabc",
# "b*a*.c*b.*"
# ))
# print(Solution.isMatch(
# "ccbbabbbabababa",
# ".*.ba*c*c*aab.a*b*"   # False
# ))
# print(Solution.isMatch(
# "bcabcbcaccabcbb",
# ".*b."))
print(Solution.isMatch(
    "bcabcbcaccabcbb",
    ".*bc*."))
# print(Solution.find_in_string("abcdcdccccddsdsabcsc", "bc.."))
# print(Solution.isMatch("aaa", "ab*a*c*a"))
# print(Solution.isMatch("aaca", "ab*a*c*a"))
# print(Solution.isMatch(
# "cabbbbcbcacbabc",
# ".*b.*.a.*c"))
# print(Solution.isMatch("bbbcbcacbabc",".*.a.*c"))
#
# print(Solution.isMatch(
# "abbaaaabaabbcba",
# "a*.*ba.*c*..a*.a*."))


# pt="a*.*b.ab*c*b*a*a*.*b*.*cc*"
# simple, concise, dot, min_len = Solution.parse_pattern(pt)
# print(pt)
# print(" simple:",simple)
# print("concise:",concise)
# print("dot asterisk:", dot)
# print("Min string chars:",min_len)
