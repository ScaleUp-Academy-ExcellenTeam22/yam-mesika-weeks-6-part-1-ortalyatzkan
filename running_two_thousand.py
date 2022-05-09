import time
from typing import Tuple, List, Callable


def timer(f: Callable, *non_keyword_var: Tuple, **keyword_var: Tuple) -> time:
    """
    A function that receives a function and parameters and return how long time a function f ran when the same parameter
    s are passed to it.
    :param f:The function for running and calculating its time.
    :param non_keyword_var:A non key worded variable-length argument list to function f.
    :param keyword_var:A key worded variable-length argument list to function f.
    :return:How long time a function f ran when the same parameters are passed to it.
    """
    start_time = time.time()
    f(*non_keyword_var, **keyword_var)
    end_time = time.time()
    return end_time-start_time


if __name__ == '__main__':
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
