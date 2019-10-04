def local_minima(alist, n):
    delta = (n - 1) // 2
    result = []

    for i in range(len(alist)):
        border_l = i - delta
        if border_l < 0:
            border_l = 0
        border_r = i + delta + 1
        if border_r > len(alist):
            border_r = len(alist)

        delta_min = min(alist[border_l:border_r])
        for j in range(border_l, border_r):
            if alist[j] == delta_min:
                temp_border_l = j - delta
                if temp_border_l < 0:
                    temp_border_l = 0
                temp_border_r = j + delta + 1
                if temp_border_r > len(alist):
                    temp_border_r = len(alist)
                if min(alist[temp_border_l:temp_border_r]) == delta_min and j == alist.index(delta_min, temp_border_l, temp_border_r):
                    result.append((alist[j], j))
                    break

    return sorted(list(set(result)), key=lambda i: i[1])
