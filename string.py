def compare(words):
    ctr = 0
    for i in words:
        if len(i) > 2 and i[0] == i[-1]:
            ctr+= 1
    return ctr

print(compare(['abc', 'xyz', 'aba', '1221']))