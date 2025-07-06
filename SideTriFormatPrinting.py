def tri_format_print(s):
    custom = "".join([item for item in s if item != ' '])
    custom = list(custom)
    while len(custom) < 3:
        custom.append("*")
    while (len(custom)) % 6 != 0:
        custom.append("*")

    subs_list = []
    count = -1
    flag = True
    print(len(custom))
    length = (len(custom) // 3) - 1
    while custom:
        if count == -1:
            count = 0
            subs_list.append([custom.pop(0)])
        else:
            if count % 2 == 0 or count == 0:
                sub_list = [" "]
            else:
                sub_list = [custom.pop()]
            for i in range(count):
                sub_list.append(" ")
            if custom:
                sub_list.append(custom.pop(0))
            if count == length:
                flag = False
            if flag:
                count += 1
            else:
                count -= 1
            subs_list.append(sub_list)

    # Normal
    for subs in subs_list:
        print()
        for sub in subs:
            print(sub, end=" ")

    max_length = 0
    for sublist in subs_list:
        if len(sublist) > max_length:
            max_length = len(sublist)

    for subs in subs_list:
        while len(subs) < max_length:
            subs.append(" ")

    # Reverse
    print("\n")
    for subs in subs_list:
        print()
        for sub in subs[::-1]:
            print(sub, end=" ")


tri_format_print("*" * 67)
