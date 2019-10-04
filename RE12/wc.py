def wc(filename):
    flp = open(filename)
    lines = words = chars = 0
    for i in flp:
        lines += 1
        words += len(i.strip("\n").strip(" ").split(" "))
        chars += len(i)
    flp.close()
    return (lines, words, chars)
