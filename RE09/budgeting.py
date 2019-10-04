def budgeting(budget, products, wishlist):
    temp = 0
    for i in wishlist:
        temp += wishlist[i] * products[i]

    while temp > budget:
        min_wish = min(wishlist, key=lambda i: products[i])
        temp = 0
        for i in wishlist:
            if i == min_wish:
                wishlist[i] -= 1
            temp += wishlist[i] * products[i]

        if wishlist[min_wish] == 0:
            del(wishlist[min_wish])
    return wishlist
