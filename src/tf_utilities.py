import numpy as np


def turn_strings_into_vectors(strings):
    unique_strings_set = set(strings)
    unique_strings = sorted(list(unique_strings_set))

    vectors = np.identity(len(unique_strings))
    return unique_strings, vectors
