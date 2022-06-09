def solution(data, n):
    n_dict = {}
    for index in range(len(data)):
        try:
            n_dict[data[index]][0] += 1
            n_dict[data[index]][1].append(index)
        except KeyError:
            n_dict[data[index]] = [1, [index]]
    for key in n_dict.keys():
        if n_dict[key][0] > n:
            for index in n_dict[key][1]:
                data[index] = None
    return [elem for elem in data if elem]