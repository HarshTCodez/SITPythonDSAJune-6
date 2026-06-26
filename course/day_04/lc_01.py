def two_sum(arr: list, target: int):
    map = {}

    for index, value in arr:
        diff = target - value
        if diff in map:
            return [index, map[diff]]
        map[value] = index

    return []
