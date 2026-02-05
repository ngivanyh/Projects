# perfect odd numbers are defined as numbers where they all consist of odd numbers
# e.g. 135, 7, 999999; not perfect odd numbers: 2, 107

DIGITS = tuple("0123456789")

while True:
    try: num = input() # we assume the input will be all characters
    except Exception: break

    additive_perfect_num = []
    for i, n in enumerate(num):
        if not int(n) & 1:
            additive_perfect_num.append(DIGITS[(int(n) + 1) % 10])
            break
        additive_perfect_num.append(n)
    additive_perfect_num += [DIGITS[1]] * (len(num) - len(additive_perfect_num))
    additive_perfect_num = int("".join(additive_perfect_num))

    # bug, subtraction needs to check whether it's actually subtracting

    subtractive_perfect_num = []
    for i, n in enumerate(num):
        if not int(n) & 1:
            subtractive_perfect_num.append(DIGITS[int(n) - 1])
            break
        subtractive_perfect_num.append(n)
    subtractive_perfect_num += [DIGITS[9]] * (len(num) - len(subtractive_perfect_num))

    while int("".join(subtractive_perfect_num)) > int(num):
        str_sub_perf_num = "".join(subtractive_perfect_num)
        num_before_nines = 0
        for i in range(len(subtractive_perfect_num) - 1, -1, -1):
            if subtractive_perfect_num[i] == "9": continue
            num_before_nines = i
            break
        # print(subtractive_perfect_num, num_before_nines)
        sub_amnt = 1 if num_before_nines == 0 else 2
        subtractive_perfect_num[num_before_nines] = DIGITS[(int(str_sub_perf_num[num_before_nines]) - sub_amnt + 10) % 10]
        # print(subtractive_perfect_num)

    subtractive_perfect_num = int("".join(subtractive_perfect_num))

    diffs = [abs(additive_perfect_num - int(num)), abs(subtractive_perfect_num - int(num))]
    # print(additive_perfect_num, subtractive_perfect_num)
    print(min(diffs))