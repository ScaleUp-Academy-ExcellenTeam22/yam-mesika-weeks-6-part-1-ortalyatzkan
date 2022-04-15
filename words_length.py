def words_length(sentence:str)->list:
    """
    A function that gets a sentence and returns its words lengths.
    :param sentence:The string for calculating the lengths of the words.
    :return:List of word lengths in a string.
    """
    return [len(word) for word in sentence.split(' ')]


if __name__ == '__main__':
    sentence_for_calculating="Toto, I've a feeling we're not in Kansas anymore"
    print(words_length(sentence_for_calculating))
