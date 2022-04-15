import time


def timer(f,*args,**kwargs)->time:
    """
    A function that receives a function and parameters and return how long time a function f ran when the same parameters are passed to it.
    :param f:The function for running and calculating its time.
    :param args:A non key worded variable-length argument list to function f.
    :param kwargs:A key worded variable-length argument list to function f.
    :return:How long time a function f ran when the same parameters are passed to it.
    """
    start_time = time.time()
    f(*args,**kwargs)
    end_time = time.time()
    return end_time-start_time


if __name__ == '__main__':
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
