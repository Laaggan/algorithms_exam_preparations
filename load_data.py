def load_data1():
    data = {
        "interval1": {
            "s": 1.2,
            "f": 2,
            "v": 5
        },
        "interval2": {
            "s": 2.2,
            "f": 4,
            "v": 10
        },
        "interval3": {
            "s": 1.1,
            "f": 4,
            "v": 5
        }
    }
    return data

def load_data2():
    #s = {1.2, 1.1, 4.2, 5.0, 2.0}
    s = [1.1, 1.2, 2.0, 4.2, 5.0]
    f = [1.3, 1.8, 4.5, 4.4, 6]
    v = [5, 10, 12, 3, 4]
    return s, f, v