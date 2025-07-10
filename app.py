def parseString(js: str, ix: int):
    res = ""
    while js[ix] != '"':
        res += js[ix]
        ix += 1
    return res, ix + 1


def parseKey(js: str, ix: int):
    if js[ix] == '"':
        return parseString(js, ix + 1)
    else:
        raise Exception(f"Syntax Error at {ix}")


def parseList(js: str, ix: int):
    res = []
    while js[ix] != "]":
        item, ix = parseValue(js, ix)
        res.append(item)
        if js[ix] == ",":
            ix += 1
        elif js[ix] != "]":
            raise Exception(f"Syntax Error at {ix}")
    return res, ix + 1


def parseValue(js: str, ix: int):
    if js[ix] == "{":
        return parseObject(js, ix + 1)
    elif js[ix] == "[":
        return parseList(js, ix + 1)
    elif js[ix] == '"':
        return parseString(js, ix + 1)


def parseObject(js: str, ix: int):
    res = {}
    while js[ix] != "}":
        key, ix = parseKey(js, ix)
        if js[ix] == ":":
            val, ix = parseValue(js, ix + 1)
            res[key] = val
            if js[ix] == ",":
                ix += 1
            elif js[ix] != "}":
                raise Exception(f"Syntax Error at {ix}")
        else:
            raise Exception(f"Syntax Error at {ix}")
    return res, ix + 1


def parseJson(js: str):
    res = {}
    if js[0] == "{":
        res, ix = parseObject(js, 1)
    else:
        raise Exception("Syntax Error at 0")

    if ix < len(js):
        print("warning: extra symbols")

    return res


if __name__ == "__main__":
    tests = [
        "{}",
        '{"key1":"value1"}',
        '{"key1":"value1","key2":"value2"}',
        '{"key1":"value1","list1":[]}',
        '{"key1":"value1","list1":["listvalue1"]}',
        '{"key1":"value1","list1":["listvalue1","listvalue2"]}',
        '{"key1":"value1","list1":["listvalue1",{"listkey1":"listvalue2"}]}',
        "{}ecxrtsfdg",
        '{"key1":"value1","list1":["listvalue1",{"listkey1":"listvalue2"},["list2value1","list2value2"],"listvalue3"]}',
        '{"key1":"value1","key2":{"key3":"value2"},"key4":"value3"}',
    ]

    for ts in tests:
        print("Testing", ts)
        print(parseJson(ts))
