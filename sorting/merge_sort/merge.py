from math import floor

# fancy input handling because it's python
# while True:
#     try:
#         sort_list = [int(n) for n in input().split(" ")]
#         break
#     except ValueError:
#         continue

sort_list = [int(n) for n in open("numbers.txt").read().split(" ")]

def merge(l1: list[int], l2: list[int]):
    out = []
    # print(l1, l2, sep='\t')

    l1i, l2i = 0, 0
    while (l1i < len(l1)) and (l2i < len(l2)):
        if l1[l1i] > l2[l2i]:
            out.append(l2[l2i])
            l2i += 1
        else:
            out.append(l1[l1i])
            l1i += 1

    add_back = l1[l1i:] if l1i != len(l1) else l2[l2i:]
    # print(f"l1i: {l1i} l2i: {l2i}; should add back: {add_back}")

    # print(f"out: {out + add_back}")
    return out + add_back

def divide(l: list[int]):
    if len(l) == 1:
        # print(f"smallest unit: {l}")
        return l
    split_index = floor(len(l)/2)
    former = l[:split_index]
    latter = l[split_index:]

    # print(f"divided list: {former} {latter}")

    return merge(divide(former), divide(latter))

print(divide(sort_list))