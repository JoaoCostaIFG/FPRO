def anagrams(alist):
    alist = sorted(alist, key=lambda i: i.lower())

    def sort_vog(i):
        return i[0].lower()

    result = []
    aux = []
    for word in alist:
        word = word.replace(" ", "")
        word = word.lower()
        aux.append(sorted(word))

    flag = True
    while flag:
        flag = False
        temp_vec = []
        for i in range(len(aux)):
            if aux[i] is not None:
                temp_pal = aux[i]
                temp_vec.append(alist[i])
                aux[i] = None
                flag = True
                break

        if not flag:
            break

        for i in range(len(aux)):
            if temp_pal == aux[i]:
                aux[i] = None
                temp_vec.append(alist[i])

        result.append(temp_vec)

    return sorted(result, key=sort_vog)
