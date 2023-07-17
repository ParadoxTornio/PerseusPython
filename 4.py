a = [1, 2, 3, 2, 1]

n = []
for i in a:
    if i not in n:
        n.append(i)

print(n)

# def remove_duplicates(lst):
#     print(list(set(lst)))
#
#
# remove_duplicates([1, 2, 3, 2, 1])
