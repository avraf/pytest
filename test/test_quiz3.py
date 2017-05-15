from nose.tools import *
from pyquiz.quiz3 import *

class TestQuiz3(object):
    def test_should_handle_an_empty_list(self):
        actual = combine_anagrams(())
        assert len(actual) is 0

    def test_should_handle_simple_single_character_case_with_no_repeats(self):
        actual = combine_anagrams(('c', 'f', 'p', 'r'))
        expected = [ ["c"], ["f"], ["p"], ["r"] ]

        assert_anagram_lists_are_equal(actual, expected)

    def test_should_handle_no_repeats_but_similiar_words(self):
        actual = combine_anagrams(('positive', 'positively'))
        expected = [ ['positive'], ['positively'] ]

        assert_anagram_lists_are_equal(actual, expected)

    def test_should_handle_some_repeated_anagrams(self):
        actual = combine_anagrams(('cars', 'for', 'potatoes', 'racs', 'four', 'scar', 'creams', 'scream'))
        expected = [ sorted(["cars", "racs", "scar"]),
                      ["four"],
                      ["for"],
                      ["potatoes"],
                      sorted(["creams", "scream"]) ]

        assert_anagram_lists_are_equal(actual, expected)

    def test_should_preserve_case_when_mix_case_repeats(self):
        actual = combine_anagrams(('c', 'C', 'f', 'p', 'r', 'P'))
        expected = [ sorted(["c", "C"]), ["f"], sorted(["p", "P"]), ["r"] ]

        assert_anagram_lists_are_equal(actual, expected)

def assert_anagram_lists_are_equal(actual, expected):
    assert all(sorted(anagram_group) in expected for anagram_group in actual)
