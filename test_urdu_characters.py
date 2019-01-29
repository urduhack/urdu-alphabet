# coding: utf8
""" Test cases """
import re
from urdu_characters import URDU_ALL_CHARACTERS, URDU_ALPHABETS, URDU_DIGITS, URDU_PUNCTUATIONS, URDU_DIACRITICS
from urdu_characters import URDU_ALL_CHARACTERS_UNICODE


URDU_UNICODE_RANGE = re.compile("[^\u0600-\u06ff]+")


class TestUrduAlphabet():
    """Test cases for Urdu Alphabet"""

    def test_urdu_alphabet(self):
        """ Test urdu_alphabet"""
        for character in URDU_ALPHABETS:
            assert character in URDU_ALL_CHARACTERS
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0

    def test_urdu_digits(self):
        """ Test """
        for character in URDU_DIGITS:
            assert character in URDU_ALL_CHARACTERS
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0

    def test_urdu_punctuation(self):
        """ Test """
        for character in URDU_PUNCTUATIONS:
            assert character in URDU_ALL_CHARACTERS
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0

    def test_diacritics(self):
        """ Test """
        for character in URDU_DIACRITICS:
            assert character in URDU_ALL_CHARACTERS
            assert len(URDU_UNICODE_RANGE.findall(character)) == 0

    def test_unicode(self):
        """ Test """
        for character in URDU_ALL_CHARACTERS:
            assert character in URDU_ALL_CHARACTERS_UNICODE

        for character, value in URDU_ALL_CHARACTERS_UNICODE.items():
            assert character in URDU_ALL_CHARACTERS
            assert value in URDU_ALL_CHARACTERS

        tmp = set()
        for character, value in URDU_ALL_CHARACTERS_UNICODE.items():
            tmp.add(value)

        for character in URDU_ALL_CHARACTERS:
            assert character in tmp
