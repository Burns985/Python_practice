def tri_format_print(s):
    custom = "".join([item for item in s if item != ' '])
    custom = list(custom)
    if len(custom) < 3:
        print("A tri-angle requires a string of length at least 3.\nBe mindful next time.")
    while len(custom) < 3:
        custom.append("*")
    while (len(custom)) % (len(custom)//3) != 0:
        custom.append("*")
    if len(custom) < 10:
        while len(custom) % 3 != 0:
            custom.append("*")
    length = len(custom) // 3

    l1 = custom[:length][::-1]
    l2 = custom[2 * length + 1:]
    l3 = custom[length: 2 * length + 1][::-1]

    sub_list = []
    subs_list = []
    for i in range(len(l3) * 2):
        if i == len(l3) - 1:
            sub_list.append(l1.pop())
            break
        else:
            sub_list.append(" ")

    subs_list.append(sub_list)
    count = 1

    while l1 and l2:
        subs_list.append([l2.pop(), l1.pop()])

    sub_list = []
    for l in l3:
        sub_list.append(l)
    subs_list.append(sub_list)

    for i in range(1, len(subs_list) - 1):
        curr2 = subs_list[i].pop()
        curr1 = subs_list[i].pop()
        for j in range(len(subs_list[len(subs_list) - 1]) - 1):
            if j != len(subs_list) - 1 - i:
                subs_list[i].append(" ")
            else:
                subs_list[i].append(curr1)
        for j in range(i):
            subs_list[i].append(" ")
        subs_list[i].append(curr2)

    # Normal
    for subs in subs_list[:len(subs_list) - 1]:
        print()
        for sub in subs:
            print(sub, end=" ")
    print()
    for sub in subs_list[len(subs_list)-1]:
        print(sub, end="   ")

    print("\n")
    # Reverse
    for sub in subs_list[len(subs_list) - 1]:
        print(sub, end="   ")
    for subs in subs_list[:len(subs_list) - 1][::-1]:
        print()
        for sub in subs:
            print(sub, end=" ")


tri_format_print("my name is umar ya know?")
