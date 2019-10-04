def isomorphic(astring1, astring2):
    result = []
    char_map = {}
    cmp_char_map = {}
    for i in range(len(astring1)):
        if astring1[i] not in char_map:
            char_map[astring1[i]] = astring2[i]
            result.append((astring1[i], astring2[i]))
        else:
            if char_map[astring1[i]] != astring2[i]:
                return "'{}' and '{}' are not isomorphic".format(astring1, astring2)

    for i in char_map:
        if char_map[i] in cmp_char_map:
            return "'{}' and '{}' are not isomorphic".format(astring1, astring2)
        else:
            cmp_char_map[char_map[i]] = i
    return "'{}' and '{}' are isomorphic because we can map: {}".format(astring1, astring2, result)
