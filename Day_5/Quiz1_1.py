def type_dict(data):

    res_dict = {}
    data_types = list(set(type(i) for i in data))

    for _type in data_types:
        for element in data:
            if (type(element) == _type):
                res_dict.setdefault(_type, []).append(element)

    return res_dict


type_dict([1, 1.3, 7, 4.4, "hi", [0, 1], "45"])
