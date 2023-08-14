#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (None, None)
    length = len(sentence)
    first_character = sentence[0]
    return (length, first_character)
