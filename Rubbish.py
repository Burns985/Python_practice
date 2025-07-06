def rect_printing(chars, length, width):
    flag = True
    sub_list = list([item for item in chars if item != ' '][::-1])
    up_list = []
    flag = True
    rev = False
    while sub_list:
        try:
            if flag:
                sub = []
                for i in range(length):
                    if sub_list:
                        sub.append(sub_list.pop())
                    else:
                        sub.append(" ")
                if rev:
                    up_list.append(sub[::-1])
                else:
                    up_list.append(sub)
                rev = not rev
            else:
                for i in range(width):
                    sub = []
                    for j in range(length):
                        if j == length - 1:
                            sub.append(sub_list.pop())
                        else:
                            sub.append(" ")
                    up_list.append(sub)
            flag = not flag
        except IndexError:
            pass
    for up in up_list:
        print()
        for u in up:
            print(u, end=" ")


rect_printing("my name is umar, ya know?", 5, 3)
