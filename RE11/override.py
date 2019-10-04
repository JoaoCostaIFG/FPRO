def override(l1, l2):
    return sorted([i for i in l1 if i[0] not in [j[0] for j in l2]] + l2)