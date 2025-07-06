class Solution:
    def lemonadeChange(self, bills: [int]) -> bool:
        change_list = []
        while bills != []:

            if (bills[0] == 5):
                change_list.append(bills.pop(0))

            elif (bills[0] == 10):
                change_list.append(bills.pop(0))
                if 5 in change_list:
                    i = change_list.index(5)
                    change_list.pop(i)
                else:
                    return False

            elif (bills[0] == 20):
                change_list.append(bills.pop(0))
                if (5 in change_list) and (10 in change_list):
                    i = change_list.index(5)
                    change_list.pop(i)
                    j = change_list.index(10)
                    change_list.pop(j)
                else:
                    a = 0
                    for change in change_list:
                        if change == 5:
                            a += 1
                    if a > 2:
                        i = change_list.index(5)
                        change_list.pop(i)
                        i = change_list.index(5)
                        change_list.pop(i)
                        i = change_list.index(5)
                        change_list.pop(i)
                    else:
                        return False
        return True