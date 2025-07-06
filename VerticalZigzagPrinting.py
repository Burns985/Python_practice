def format_printing(g_list, num_lists):
    if num_lists <= 0:
        print("Columns are only in natural numbers")
        return
    if num_lists == 1:
        for g in g_list:
            if g != " ":
               print(g, end=" ")
    else:
        fla = True
        flag = True
        f_list = list(g_list)

        updated_list = [item for item in f_list if item != ' ']
        updated_list = updated_list[::-1]

        list_dict = {}
        for i in range(num_lists):
            list_dict[f"list_{i+1}"] = []

        try:
            flag = True
            while updated_list:
                if flag:
                    for key in list_dict.keys():
                        curr = list_dict[key]
                        curr.append(updated_list.pop())
                        list_dict[key] = curr
                    flag = False
                else:
                    a = list(list_dict.keys())
                    a = a[1:len(a) - 1]
                    a = a[::-1]
                    i = 0
                    m = len(a) - 1
                    for key in a:
                        curr = list_dict[key]
                        for j in range(i):
                            curr.append(" ")
                        i += 1
                        curr.append(updated_list.pop())
                        for n in range(m):
                            curr.append(" ")
                        m -= 1
                        list_dict[key] = curr

                    for i in list_dict.keys():
                        if i not in a:
                            curr = list_dict[i]
                            for k in range(num_lists - 2):
                                curr.append(" ")
                            list_dict[i] = curr
                    flag = True

        except IndexError:
            fla = False
            for i in list_dict:
                print()
                for j in list_dict[i]:
                    print(j, end=" ")

        if fla:
            for i in list_dict:
                print()
                for j in list_dict[i]:
                    print(j, end=" ")


format_printing("my na,,,me is,,, umair", 1)
