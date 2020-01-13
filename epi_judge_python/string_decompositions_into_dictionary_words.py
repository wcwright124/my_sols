import collections

from test_framework import generic_test


def find_all_substrings(s, words):
    # TODO - you fill in here.
    def is_match(start_idx):
        curr_counts = collections.Counter()
        for i in range(start_idx, start_idx + word_len * num_words, word_len):
            curr_word = s[i:i + word_len]
            curr_counts[curr_word] += 1
            if word_freqs[curr_word] == 0 or curr_counts[curr_word] > word_freqs[curr_word]:
                return False
        return True
    word_freqs = collections.Counter(words)
    num_words = len(words)
    word_len = len(words[0])
    end = len(s) - num_words * word_len
    return [i for i in range(end + 1) if is_match(i)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "string_decompositions_into_dictionary_words.py",
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
