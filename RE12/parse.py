def parse(filename):
    with open(filename) as flp:
        lines = []
        for i in flp.readlines():
            lines += i.strip(" ").strip("\n").split(" ")

        new_lines = "("
        for i in lines:
            if i == "(":
                new_lines += i
            else:
                new_lines += i + ","
        new_lines += ")"
        new_lines = eval(new_lines)
    return new_lines
