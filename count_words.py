import re


def count_word(text: str) -> dict:
    """
    A function that gets text and returns the lengths of words in the text as a dictionary.
    :param text:Text for which the lengths of the words will be calculated.
    :return:Lengths of words in the text as a dictionary.
    """
    return {word: len(word) for word in (re.sub(r"[.\n]", ' ', text)).split(' ')if word != '' and word != '\n'}


if __name__ == '__main__':
    text_for_count_word = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print((count_word(text_for_count_word)))
