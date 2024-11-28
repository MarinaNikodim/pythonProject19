def all_variants(text):
    length = len(text)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start: end]


letters = all_variants('skills')
for i in letters:
    print(i)
'''print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))'''
