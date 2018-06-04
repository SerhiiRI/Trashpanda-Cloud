def factorial(n):
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    """
    print("Silnia z {}".format(str(n)))
    return "FACTORIAL"

def bublesort(iterabe:list):
    '''
    :param iterable:
    :return:
    '''
    print("Bombekowe sortowania dla zbioru:{}".format(str(",".join(str(x) for x in iterabe))))
    return "BUBLE SORT"

def searching(iterable:list, pattern):
    '''

    :param iterable:
    :param pattern:
    :return:
    '''
    print("Bombekowe sortowania dla zbioru:{} wedlug patternu {}".format(str(",".join(str(x) for x in iterable)), pattern))
    return "SEARCH"

functionList={
    "factorial": factorial,
    "bublesort": bublesort,
    "searching": searching
}


