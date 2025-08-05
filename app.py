def parseString(js: str, ix: int):
    res = ""
    while True:
        if ix >= len(js):
            raise Exception("The json string finished prematurely")
        if js[ix] == '"':
            break
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
    while True:
        if ix >= len(js):
            raise Exception("The json string finished prematurely")
        if js[ix] == "]":
            break
        item, ix = parseValue(js, ix)
        if ix >= len(js):
            raise Exception("The json string finished prematurely")
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
    while True:
        if ix >= len(js):
            raise Exception("The json string finished prematurely")
        if js[ix] == "}":
            break
        key, ix = parseKey(js, ix)
        if ix >= len(js):
            raise Exception("The json string finished prematurely")
        if js[ix] == ":":
            val, ix = parseValue(js, ix + 1)
            if ix >= len(js):
                raise Exception("The json string finished prematurely")
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
    if len(js) > 0 and js[0] == "{":
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
        '{"key1":"value1","key2":{"key3":"va',
        '{"key1":"value1","key2":{"key3":"value2"},"key4":"value3"',
        '{"key1":"value1","list1":["listvalue1",{"listkey1":"listvalue2"},["list2value1","list2value2"],"listvalue3"',
        '{"key1":"value1",a"key2":"value2"}',
        '{"key1":"value1","list1":[',
        '{"key1":"value1","key2":{',
    ]

    for ts in tests:
        print("Input:", ts)
        try:
            print("Output:", parseJson(ts))
        except Exception as e:
            print("Error:", e)
