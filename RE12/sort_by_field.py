def sort_by_field(filename, field):
    with open(filename) as flp:
        temp = flp.readlines()
        header = temp[0]
        temp = temp[1:]
        ind = header.strip("\n").split(",").index(field)
        temp = sorted(temp, key=lambda i: i.split(",")[ind])
        for i in temp:
            header += i.strip("\n") + "\n"
    return header
