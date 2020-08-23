import itertools


def recurse(pref, suff, res):
    if suff == "":
        res.append(pref)
        return
    if suff[0].lower() == suff[0].upper():
        recurse(pref + suff[0], suff[1:], res)
    else:
        recurse(pref + suff[0].lower(), suff[1:], res)
        recurse(pref + suff[0].upper(), suff[1:], res)


def mutate_word(word):
    lower_word = word.lower()
    upper_word = word.upper()
    return ["".join(c) for c in itertools.product(*zip(lower_word, upper_word))]


test_word = "line444"
m1 = mutate_word(test_word)
print(m1)
print(len(m1))
m2 = list(set(m1))
print(m2)
print(len(m2))

m3 = []
recurse("", test_word, m3)
print(m3)
print(len(m3))

m4 = zip(test_word.lower(),test_word.upper())
print(*m4)
for s in m4:
    print(s)

# with open("passwords.txt") as f:
#     for line in f:
#         print(mutate_word(line.strip()))
