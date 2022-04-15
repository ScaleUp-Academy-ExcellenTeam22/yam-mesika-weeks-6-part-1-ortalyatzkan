def get_letters()->list:
    """
    A function that returns the list of all letters between A and Z and between a and z.
    :return: list of all letters between A and Z and between a and z.
    """
    return [chr (letter) for letter in range(ord('A'),ord('Z'))] + [chr (letter) for letter in range(ord('a'),ord('z'))]


if __name__ == '__main__':
    print(get_letters())
    