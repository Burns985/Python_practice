def format_printing(g_list, num_lists):
    if num_lists <= 0:
        print("Rows are only in natural numbers")
        return
    if num_lists == 1:
        for g in [item for item in g_list if item != ' ']:
            print(g)
    else:
        flag = True
        f_list = list(g_list)
        l_list = []
        updated_list = [item for item in f_list if item != ' ']
        updated_list = updated_list[::-1]
        fla = True
        while updated_list:
            try:
                if flag:
                    s_list = []
                    for i in range(num_lists):
                        if updated_list:
                            s_list.append(updated_list.pop())
                    l_list.append(s_list)

                else:
                    i = num_lists - 1
                    while i != 1:
                        t_list = []
                        for j in range(i):
                            if j == i - 1:
                                t_list.append(updated_list.pop())
                            else:
                                t_list.append(" ")
                        i -= 1
                        l_list.append(t_list)
                flag = not flag
            except IndexError:
                fla = False
                for a in l_list:
                    print()
                    for b in a:
                        print(b, end=" ")
        if fla:
            for a in l_list:
                print()
                for b in a:
                    print(b, end=" ")


format_printing("my name is umar", 4)
