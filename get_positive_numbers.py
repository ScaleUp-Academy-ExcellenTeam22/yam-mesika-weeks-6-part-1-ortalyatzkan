def get_positive_numbers()->list:
    """
    A function that gets a list of numbers from the user.
    The function returns the positive numbers it get in the user's input.
    :return:A list of the positive numbers in the user's input.
    """
    list_of_int = [int(user_input) for user_input in input("Please enter a list of numbers separated by ',' :").split(',')]
    return list(filter(lambda number_input:number_input > 0, list_of_int))


if __name__ == '__main__':
    print(get_positive_numbers())
