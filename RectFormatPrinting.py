def divide_string(s, n):
    if len(s) % 2 != 0:
        s += '*'
    end_length = (len(s) - n) // 2

    first_part = s[:end_length]
    middle_part = s[end_length:end_length + n]
    last_part = s[-end_length:]

    return first_part, middle_part, last_part


def rect_format_print(s):
    if len(s) < 6:
        print("A rectangle requires a string of length at least 6.\nBe mindful next time.")
    while len(s) < 6:
        s += "*"
    custom = "".join([item for item in s if item != ' '])
    custom = list(custom)
    flag = True
    length = len(custom) // 3
    l1 = custom[:length]
    w1, l2, w2 = divide_string(custom[length:], length)
    w2 = w2[::-1]
    for l in l1:
        print(l, end=" ")
    print()
    for i in range(0, len(w1)):
        print(w2[i], end=" ")
        for j in range(length - 2):
            print(" ", end=" ")
        print(w1[i])
    for l in l2[::-1]:
        print(l, end=" ")
    print("\n")


print("Welcome to Rectangle format printer.\n")
while True:
    c = input("Please enter string to print.\nOr\nPress '0' to quit\n")
    if c == "0":
        print("Thank you for using our service.\nWe hope you have a lovely rest of the day.")
        break
    else:
        rect_format_print(c)
