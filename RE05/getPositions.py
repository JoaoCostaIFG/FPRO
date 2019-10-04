def get_positions(word_list, sentence):
    result = ""
    flag = False
    word1 = word2 = ""
    for i in range(len(sentence)):
        if sentence[i] == " ":
            flag = True
            continue
        if flag:
            word2 += sentence[i]
        else:
            word1 += sentence[i]

    for i in range(len(word_list)):
        if word1 == word_list[i]:
            result += (str(i) + " ")
            break

    for i in range(len(word_list)):
        if word2 == word_list[i]:
            result += str(i)
            break

    return result


print(get_positions(["hello", "world", "lousy"], "lousy world"))
