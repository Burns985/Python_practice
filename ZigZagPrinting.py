def z_format(g_list, num_lists):
    if num_lists <= 0:
        print("Columns are only in natural numbers")
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


def reverse_z_format(g_list, num_lists):
    if num_lists <= 0:
        print("Columns are only in natural numbers")
        return
    if num_lists == 1:
        for g in [item for item in g_list if item != ' '][::-1]:
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
                    l_list.append(s_list[::-1])

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
                        while len(t_list) != num_lists:
                            t_list.append(" ")
                        l_list.append(t_list[::-1])
                flag = not flag
            except IndexError:
                fla = False
                max_length = len(max(l_list, key=len))
                for sl in l_list:
                    while len(sl) < max_length:
                        sl.insert(0, " ")
                for sl in l_list:
                    print()
                    for ls in sl:
                        print(ls, end=" ")
        if fla:
            max_length = len(max(l_list, key=len))
            for sl in l_list:
                while len(sl) < max_length:
                    sl.insert(0, " ")
            for sl in l_list:
                print()
                for ls in sl:
                    print(ls, end=" ")


def n_format(g_list, num_lists):
    if num_lists <= 0:
        print("Columns are only in natural numbers")
        return
    if num_lists == 1:
        for g in g_list:
            if g != " ":
                print(g, end=" ")
    else:
        fla = True
        f_list = list(g_list)

        updated_list = [item for item in f_list if item != ' ']
        updated_list = updated_list[::-1]

        list_dict = {}
        for i in range(num_lists):
            list_dict[f"list_{i + 1}"] = []

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


def reverse_n_format(g_list, num_lists):
    if num_lists <= 0:
        print("Columns are only in natural numbers")
        return
    if num_lists == 1:
        for g in g_list[::-1]:
            if g != " ":
                print(g, end=" ")
    else:
        fla = True
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
                        if updated_list:
                            curr.append(updated_list.pop())
                        else:
                            curr.append(" ")
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
            sublist = []
            for i in list_dict:
                sublist.append(list_dict[i][::-1])
            max_length = len(max(sublist, key=len))
            for sl in sublist:
                while len(sl) < max_length:
                    sl.insert(0, " ")
            for sl in sublist:
                print()
                for ls in sl:
                    print(ls, end=" ")

        if fla:
            sublist = []
            for i in list_dict:
                sublist.append(list_dict[i][::-1])
            max_length = len(max(sublist, key=len))
            for sl in sublist:
                while len(sl) < max_length:
                    sl.insert(0, " ")
            for sl in sublist:
                print()
                for ls in sl:
                    print(ls, end=" ")


while True:
    c = input("\n\nWelcome to ZigZag printer.\n"
              "\nPlease choose a printing format:"
              "\n1: Z format\n2: Reverse Z format"
              "\n3: N format\n4: Reverse N format\n5: Quit\n")
    while True:
        if c.isdigit() and (1 <= int(c) <= 5):
            break
        print("Wrong! Please enter one of the available options")
        c = input("\nPlease choose a printing format:"
                  "\n1: Z format\n2: Reverse Z format"
                  "\n3: N format\n4: Reverse N format\n5: Quit\n")
    if c != "5":
        s = input("Please enter string to format:\n")
        if int(c) > 2:
            while True:
                rc = input("Please enter number of rows: ")
                if rc.isdigit() and 0 < int(rc) < len(s):
                    break
                if rc.isdigit() and int(rc) >= len(s):
                    print("\nNumber of rows may not equate to or exceed length of provided string")
                print("Invalid input. Please try again.")
        else:
            while True:
                rc = input("Please enter number of columns: ")
                if rc.isdigit() and 0 < int(rc) < len(s):
                    break
                if rc.isdigit() and int(rc) >= len(s):
                    print("\nNumber of columns may not equate to or exceed length of provided string")
                print("Invalid input. Please try again.")

    if c == "1":
        z_format(s, int(rc))
    if c == "2":
        reverse_z_format(s, int(rc))
    if c == "3":
        n_format(s, int(rc))
    if c == "4":
        reverse_n_format(s, int(rc))
    if c == "5":
        print("Thank you for using our product.\nWe hope you have a lovely rest of your day...")
        break

    choice = input("\n\nPress 'N' to quit\n")
    if choice == 'n' or choice == 'N':
        print("Thank you for using our product.\nWe hope you have a lovely rest of your day...")
        break
