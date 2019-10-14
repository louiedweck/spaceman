from spaceman import *
import unittest


class SpacemanTest(unittest.TestCase):
    def test_load_word(self):
        random_word = load_word()
        assert len(random_word) > 0
        assert type(random_word) == str

    def test_is_word_guessed(self):
        assert is_word_guessed("hello", ['h', 'e', 'l', 'o']) is True
        assert is_word_guessed("hello", ['h', 'e', 'l']) is False

    def test_is_guess_in_word(self):
        g_in_goon = is_guess_in_word('g', 'goon')
        assert g_in_goon is True
        z_in_apple = is_guess_in_word('z', 'apple')
        assert z_in_apple is False

    def test_find_indicies(self):
        assert find_indicies("alpha", 'p') == [2]
        assert find_indicies("aaaaa", 'a') == [0, 1, 2, 3, 4]
        assert find_indicies("alpha", 'z') == []
