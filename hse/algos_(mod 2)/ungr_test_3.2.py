def subsets(elems):
    if not elems:
        return [[]]

    print(elems[:-1])
    result = subsets(elems[:-1])

    last = elems[-1]

    for i in range(len(result)):
        result.append(result[i] + [last])

    return result


print(subsets(range(12))[13])

