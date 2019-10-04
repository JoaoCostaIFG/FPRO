def mastermind(g1, g2, g3, c1, c2, c3):
    points = 0
    # "b"=1 "w"=2 "y"=3 "taken"=0
    comp_array = [c1, c2, c3]
    for i in range(3):
        if g1 == comp_array[i]:
            if i == 0:
                points += 3
            else:
                points += 1
            comp_array[i] == " "
            break

    for i in range(3):
        if g2 == comp_array[i]:
            if i == 1:
                points += 3
            else:
                points += 1
            comp_array[i] == " "
            break

    for i in range(3):
        if g3 == comp_array[i]:
            if i == 2:
                points += 3
            else:
                points += 1
            comp_array[i] == " "
            break

    return points


print(mastermind('b', 'b', 'y', 'b', 'w', 'b'))
