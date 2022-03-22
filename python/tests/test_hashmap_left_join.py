from code_challenges.hash.hashmap_left_join import hash_left_join
import pytest

def test_import():
    assert hash_left_join

def test_hash_left_join():
    synonyms = {'happy': 'joyful'}
    antonyms = {'happy': 'sad'}
    assert hash_left_join(synonyms, antonyms) == ['happy', 'joyful', 'sad']

def test_hash_left_join_more():
    synonyms = {'happy': 'joyful','scared':'afraid'}
    antonyms = {'happy': 'sad','scared':'brave'}

    assert hash_left_join(synonyms, antonyms) == ['happy', 'joyful', 'sad', 'scared', 'afraid', 'brave']

def test_hash_left_join_with_none():
    synonyms = {'happy': 'joyful','scared':'afraid','mad':'angry'}
    antonyms = {'happy': 'sad','scared':'brave'}

    assert hash_left_join(synonyms, antonyms) == ['happy', 'joyful', 'sad', 'scared', 'afraid', 'brave','mad', 'angry', None]
