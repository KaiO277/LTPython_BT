from itertools import combinations

def all_subsets(lst):
    subsets = []
    for i in range(len(lst) + 1):
        for subset in combinations(lst, i):
            subsets.append(list(subset))
    return subsets

# Chạy chương trình
lst = [1, 2, 3]
subsets = all_subsets(lst)

print("Danh sách con là:")
for subset in subsets:
    print(subset)
