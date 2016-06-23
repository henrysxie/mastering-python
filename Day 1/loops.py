numbers = [1, 2, 8, 7, 9, 12]

def find_trump(names):

    for i, name in enumerate(names):
        if name == "Trump":
            return i

    return -1


print find_trump(['Clinton', 'Obama', 'Trump'])
print find_trump(['Clinton', 'Obama'])
