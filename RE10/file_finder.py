def file_finder(dirs, file_name):
    for i in dirs[1:]:
        if i == dirs[0]:
            return -1
        if i == file_name:
            return dirs[0] + "/" + file_name
    for i in dirs[1:]:
        if type(i) is list:
            temp = file_finder(i, file_name)
            if type(temp) is str:
                return dirs[0] + "/" + temp
            elif temp == -1:
                return None
