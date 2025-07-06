family_tree = {
    "John": ["Alice", "Eve"],
    "Alice": ["Bob", "Carol"],
    "Bob": ["Charlie", "David"],
    "Charlie": ["Emily", "Frank"],
    "Carol": ["Grace", "Henry"],
    "David": ["Isabel", "Jack"],
    "Grace": ["Kate", "Liam"],
    "Henry": ["Mia", "Noah"]
}


def modus_ponens(family, person):
    for child, parents in family.items():
        if parents[0]:
            return f"{child} is the child of {parents.pop()} and {parents.pop()}."
    return "Fact cannot be derived."


result = modus_ponens(family_tree, "Alice")
print(result)
