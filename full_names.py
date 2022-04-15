def full_names(first_names:list,last_names:list,min_length:int=None)->list:
    """
    A function that gets a list of first names and a list of last names and combines them.
    The function returns all combinations that are smaller than min_length.
    :param first_names:List of first names.
    :param last_names:List of last names
    :param min_length:Minimum size for combining a first name with a last name, its default value is None.
    :return:List of all combinations of first name and last name that are smaller than min_length.
    """
    return [first_name.capitalize() + " " + last_name.capitalize() for first_name in first_names
            for last_name in last_names if ((min_length is not None and len(first_name+last_name+" ") >= min_length) or min_length is None)]


if __name__ == '__main__':
    first_names_list = ['avi', 'moshe', 'yaakov']
    last_names_list = ['cohen', 'levi', 'mizrahi']

    print(full_names(first_names_list, last_names_list, 10) == ['Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi',
                                                'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi'])
    print(full_names(first_names_list, last_names_list) == ['Avi Cohen', 'Avi Levi', 'Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi',
                                            'Moshe Mizrahi', 'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi'])
