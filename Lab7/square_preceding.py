def square_preceding(values):
    """ (list of number) -> NoneType
    Replace each item in the list with square the value of the
    preceding item, and replace the first item with 0.
    >>> L = [1, 2, 3]
    >>> square_preceding(L)
    >>> L
    [0, 1, 4]
    """
    # if values != []:
    #     temp = values[0]
    #     values[0] = 0
    # for i in range(1, len(values)):
    #     values[i] = temp ** 2
    #     temp = values[i]
    res = [0,]
    for i in range(1, len(values)):
        previous = values[i-1]
        if not isinstance(previous, int) and not isinstance(previous, float):
            current = previous
        else:
            current = previous ** 2
        res.append(current)
    for i in range(len(values)):
        values[i] = res[i]