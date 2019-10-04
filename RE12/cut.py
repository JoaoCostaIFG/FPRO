def cut(filename, delimiter, field):
    result = ""
    with open(filename) as flp:
        if type(field) is list:
            for i in flp:
                temp = i.split(delimiter)
                result += temp[field[0] - 1].strip("\n")
                for j in range(1, len(field)):
                    result += delimiter + temp[field[j] - 1].strip("\n")
                result += "\n"
        else:
            for i in flp:
                result += i.split(delimiter)[field - 1].strip("\n") + "\n"
        return result
