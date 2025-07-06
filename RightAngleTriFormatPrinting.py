def pythagoras_triplets(n):
    for i in range(1, 100):
        for j in range(1, 100):
            for k in range(1, 100):
                if k**2 == j**2 + i**2 and k + j + i >= n:
                    return i, j, k


def tri_format_print(s):
    custom = "".join([item for item in s if item != ' '])
    max_width = len("".join([item for item in s if item != ' ']))
    custom = list(custom)
    base, per, hyp = pythagoras_triplets(len(custom))
    if base + per + hyp > len(custom):
        while base + per + hyp > len(custom):
            custom.append("*")
    subs_list = []
    flag = True
    count = - 1
    print(len(custom))
    while custom:
        if count == -1:
            count = 0
            subs_list.append([custom.pop(0)])
        else:
            if count % 2 != 0:
                sub_list = [custom.pop()]
            else:
                sub_list = [" "]
            for i in range(count):
                sub_list.append(" ")
            if custom:
                sub_list.append(custom.pop(0))
            count += 1
            subs_list.append(sub_list)
        if subs_list:
            print(2 * len(custom), len(subs_list[len(subs_list) - 1]))

            if 2 * len(custom) == len(subs_list[len(subs_list) - 1]) - 1:
                sub = sub_list.pop()
                while True:
                    n = sub_list.pop()
                    if n != " ":
                        sub_list.append(n)
                        break
                while custom:
                    sub_list.append(custom.pop())
                sub_list.append(sub)
                break

            if 2 * len(custom) + 1 <= len(subs_list[len(subs_list) - 1]) + 4:
                break
    sub_list = []
    for cus in custom[::-1]:
        sub_list.append(cus)
    subs_list.append(sub_list)

    for subs in subs_list[:len(subs_list) - 1]:
        print()
        for sub in subs:
            print(sub, end=" ")
    print()
    for sub in subs_list[len(subs_list) - 1]:
        print(sub, end="   ")


    # Contrastive
    max_length = 0
    for sublist in subs_list:
        if len(sublist) > max_length:
            max_length = len(sublist)

    for subs in subs_list[: len(subs_list) - 1]:
        while len(subs) < max_length:
            subs.append(" ")

    print("\n")
    print()
    for sub in subs_list[len(subs_list) - 1][::-1]:
        if " " != sub:
            print(sub, end="   ")
    for subs in subs_list[:len(subs_list) - 1][::-1]:
        for i in range(2, int(max_width ** 0.5) + 1):
            if max_width % i == 0:
                flag = False
        if not flag:
            subs.append(" ")
        print()
        for sub in subs[::-1]:
            print(sub, end=" ")

    # Down top
    print("\n")
    for sub in subs_list[len(subs_list) - 1]:
        print(sub, end="   ")
    for subs in subs_list[:len(subs_list) - 1][::-1]:
        print()
        for sub in subs:
            print(sub, end=" ")

    # Horizontal reverse
    for subs in subs_list[:len(subs_list) - 1]:
        print()
        for sub in subs[::-1]:
            print(sub, end=" ")
    print()
    for sub in subs_list[len(subs_list) - 1][::-1]:
        if sub != " ":
            print(sub, end="   ")


tri_format_print("a" * 13)
