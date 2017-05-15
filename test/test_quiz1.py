from nose.tools import *
from pyquiz.quiz1 import *

class TestQuiz1(object):
    def test_is_palindrome_should_pass_empty_string(self):
        assert is_palindrome('')

    def test_is_palindrome_should_pass_string_with_non_word_chars_and_mix_cases(self):
        assert is_palindrome("Madam, I'm Adam!")

    def test_is_palindrome_should_fail_when_not_palindrome(self):
        assert_false(is_palindrome("Abracadabra"))

    def test_count_words_should_handle_empty_string(self):
        assert not any(count_words(''))

    def test_count_words_should_return_dict_of_words_and_appearances_as_key_value(self):
        expected = {'doo': 3, 'bee': 2}
        assert_equal(expected, count_words('Doo bee doo bee doo'))

    def test_count_words_should_ignore_non_word_chars_and_mix_cases(self):
        expected = {'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama': 1}
        assert_equal(expected, count_words("A man, a plan, a canal -- Panama"))
