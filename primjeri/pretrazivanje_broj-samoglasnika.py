def samoglasnici(s):
    bs = 0
    for i in s:
        if i in 'aeiou':
            bs += 1
    return bs


