from test_framework import generic_test


def find_nearest_repetition(paragraph):
    # TODO - you fill in here.
    min_repeat_distance = float('inf')
    recent_word_dict = {}
    for idx, word in enumerate(paragraph):
        if word in recent_word_dict:
            current_repeat_distance = idx - recent_word_dict[word]
            min_repeat_distance = min(min_repeat_distance, current_repeat_distance)
        recent_word_dict[word] = idx
    if min_repeat_distance == float('inf'):
        return -1
    return min_repeat_distance


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
