import itertools

# 判断 word 是不是一个回文
def is_palindrome(word: str) -> bool:
    new_word = reversed([x for x in word])
    new_one = ''.join(new_word)
    if new_one == word:
        return True
    else:
        return False


# 根据s字符串所含的字符，生成可能产生的字符串的组合
# 例如 s='ab', 则可能产生 'ab','ba' 两种可能的字符串
def perm(s: str = '') -> set:
    if len(s) <= 1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in perm(s[0:i]+s[i+1:]):
             sl.append(s[i]+j)

    return set(sl)


def word_collection(word: str) -> list:
    return [c for c in itertools.product(word, repeat=len(word))]


# 产生 word 的全部大小写组合，字母顺序不变
def variant_word(word: str) -> list:
    # zip 和 enumerate 类似，enumerate 默认从 0 开始与 list 并行，实际上是元组(0,elem)； 而 zip 每次从一个 iterable 里取一个元素并行组成元组
    return [''.join(c) for c in itertools.product(*zip(word.lower(),word.upper()))]

# 求一个字符串的各种组合下，有多少次是回文
def distinctPalindromes(S: str) -> int:
    if 1 <= len(S) <= 30:
        rs = list(filter(is_palindrome, perm(S)))
        return len(rs)
    else:
        # this is default OUTPUT. You can change it.
        return -404


# INPUT [uncomment & modify if required]
S = str(input())

print(distinctPalindromes(S))

print(variant_word('word'))

print(word_collection('wov'))

ss = 'flow'
print(zip(ss.lower(),ss.upper()))