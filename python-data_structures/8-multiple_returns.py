#!/usr/bin/python3
def multiple_returns(sentence):
    """ returns a tuple with the length of a string and its first character"""
    if sentence == 0:
        return (None)

    return (len(sentence), sentence[0])
