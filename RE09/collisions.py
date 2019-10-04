def collisions(alist):
    hashes = {}
    for i in alist:
        temp = 0
        while i > 0:
            temp += i % 10
            i = i // 10
        temp = temp % 8
        if temp in hashes:
            hashes[temp] += 1
        else:
            hashes[temp] = 1
    return hashes
