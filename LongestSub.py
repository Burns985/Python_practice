def long_substring(os):
   
    limit = len(os)
    visited = set()
    start = end = max_length = max_start = max_end = 0

    while end < limit:
        if os[end] not in visited:
            visited.add(os[end])
            end += 1
        else:
            if end - start > max_length:
                max_length = end - start
                max_start = start
                max_end = end - 1

            visited.remove(os[start])
            start += 1

    if end - start > max_length:
        max_length = end - start
        max_start = start
        max_end = end - 1

    long_sub = os[max_start:max_end + 1]
    print("Longest substring:", long_sub)

    return max_length


os = "the lazy man is not active"
l = long_substring(os)
print("Length of the longest substring:", l)
