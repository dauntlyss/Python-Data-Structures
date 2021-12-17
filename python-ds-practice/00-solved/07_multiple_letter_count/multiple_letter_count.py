def multiple_letter_count(phrase):
    dctnry = dict()
    for letter in phrase:
        dctnry[letter] = dctnry.get(letter, 0) + 1
    return dctnry

    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """