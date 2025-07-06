def remove_duplicates(input_list):
    return list(set(input_list))


original_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(original_list)
print(result)
