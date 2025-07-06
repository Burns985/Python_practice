def charCount(s):
    counter = {}
    for char in s:
        if char in counter:
            val = counter[char]
            val += 1
            counter[char] = val
        else:
            counter[char] = 1
    return counter


print(charCount("please"))
