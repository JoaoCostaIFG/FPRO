def manipulator(l, cmds):
    result = ""
    temp_str = l.copy()
    for cmd in cmds:
        if cmd[0:3] == "rem":
            temp_str.remove(int(cmd[7:]))
        elif cmd[0:3] == "rev":
            temp_str = temp_str[::-1]
        elif cmd[0:2] == "pr":
            result += str(temp_str) + " "
        elif cmd[0:2] == "po":
            del temp_str[-1]
        elif cmd[0] == "i":
            insert_unpack = cmd.split()
            temp_str.insert(int(insert_unpack[1]), int(insert_unpack[2]))
        elif cmd[0] == "a":
            temp_str.append(int(cmd[7:]))
        else:
            # sort
            temp_str = sorted(temp_str)
    return result
