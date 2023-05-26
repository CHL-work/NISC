import pytest
import count_occurrences 

def test_single_word():
    assert count_occurrences.count_occurrences("hello") == [('e', 1), ('h', 1), ('l', 2), ('o', 1)]

def test_sentence():
    assert count_occurrences.count_occurrences("Typical Sentence") == [(' ', 1), ('S', 1), ('T', 1), ('a', 1), ('c', 2), ('e', 3), ('i', 1), ('l', 1), ('n', 2), ('p', 1), ('t', 1), ('y', 1)]

def test_special_characters():
    assert count_occurrences.count_occurrences("!@#$%^&*()") == [('!', 1), ('#', 1), ('$', 1), ('%', 1), ('&', 1), ('(', 1), (')', 1), ('*', 1), ('@', 1), ('^', 1)]

def test_empty_string():
    assert count_occurrences.count_occurrences("") == []

def test_numbers():
    assert count_occurrences.count_occurrences("1234567890") == [('0', 1), ('1', 1), ('2', 1), ('3', 1), ('4', 1), ('5', 1), ('6', 1), ('7', 1), ('8', 1), ('9', 1)]

def test_non_ascii_characters():
    assert count_occurrences.count_occurrences("héllo") == [('h', 1), ('l', 2), ('o', 1)]
