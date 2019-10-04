def budgeting2(budget, products, wishlist):
    def val_calc(binind):
        temp = ""
        binind_i = binind.index("1")
        temp = binind.replace("1", "0", 1)
        if memo[temp] == -1:
            return -1
        return memo[temp] + full_list[int(binind_i)][0]

    full_list = []
    max_ind = 0
    for i in wishlist:
        max_ind += wishlist[i]
        for j in range(wishlist[i]):
            full_list.append((products[i], i))

    memo = {}
    memo["".rjust(max_ind, "0")] = 0
    maximum = 0
    maximum_ind = 0
    for i in range(1, 2**max_ind):
        temp = bin(i)[2:].rjust(max_ind, "0")
        memo[temp] = val_calc(temp)
        if memo[temp] > budget:
            memo[temp] = -1
        elif memo[temp] > maximum:
            maximum = memo[temp]
            maximum_ind = temp

    memo = {}
    for i in range(len(maximum_ind)):
        if maximum_ind[i] == "1":
            try:
                memo[full_list[i][1]] += 1
            except KeyError:
                memo[full_list[i][1]] = 1

    return memo
