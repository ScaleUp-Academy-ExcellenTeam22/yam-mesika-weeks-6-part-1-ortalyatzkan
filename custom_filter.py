def my_filter(function, iterable):
    """
    A Function that receives iterable and  function.
    The function returns a new iterable,
    that contains all the values in iterable for which the function it received returns a value equal to true.
    :param function:A function that works on the iterable values or None.
    :param iterable:The iterable on which the function works.
    :return:The values for which the function returns a value equal to true.
    """
    yield from[item for item in iterable if function is not None and function(item) or function is None and item]


if __name__ == '__main__':
    numbers = [1, -3, 10, 20, -10, 56, 84, -30]
    mature_ages = my_filter(lambda number:number > 0, numbers)
    print(tuple(mature_ages))
    mature_ages = my_filter(None, numbers)
    print(tuple(mature_ages))
