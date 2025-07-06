def first_and_last(input_list):
    if len(input_list) < 2:
        return "List should have at least two elements"
    else:
        return [input_list[0], input_list[-1]]


a = [5, 10, 15, 20, 25]
result = first_and_last(a)
print(result)
