from code_challenges.hash.hashtable import Hashtable


def test_hashtable():
    assert Hashtable

def test_hash():
    # Successfully hash a key to an in-range value
    hasht = Hashtable()
    actual = hasht.hash('dog')
    expected = 778
    assert actual == expected

def test_hash_not_working():
    hasht = Hashtable()
    actual = hasht.hash('dog')
    expected = 763
    assert actual != expected

def test_set():
    # Setting a key/value to your hashtable results in the value being in the data structure
    hasht = Hashtable()
    hasht.set('dog', 'kaysee')
    actual = hasht.buckets[778]
    expected = [('dog', 'kaysee')]
    assert actual == expected

def test_set_collision():
    # Successfully handle a collision within the hashtable
    hasht = Hashtable()
    hasht.set('dog', 'kaysee')
    hasht.set('god', 'God')
    actual = hasht.buckets[778]
    expected = [('dog', 'kaysee'),('god', 'God')]
    assert actual == expected

def test_get():
    # Retrieving based on a key returns the value stored
    hasht = Hashtable()
    hasht.set('dog', 'kaysee')
    actual = hasht.get('dog')
    expected = 'kaysee'
    assert actual == expected

def test_get_collision():
    # Successfully retrieve a value from a bucket within the hashtable that has a collision
    hasht = Hashtable()
    hasht.set('dog', 'kaysee')
    hasht.set('god', 'God')
    actual1 = hasht.get('dog')
    expected1 = 'kaysee'
    actual2 = hasht.get('god')
    expected2 = 'God'
    assert actual1 == expected1
    assert actual2 == expected2

def test_get_null():
    # Successfully returns null for a key that does not exist in the hashtable
    hasht = Hashtable()
    hasht.set('dog', 'kaysee')
    actual = hasht.get('cat')
    expected = None
    assert actual == expected

def test_contains_true():
    hasht = Hashtable()
    hasht.set('dog', 'kaysee')
    actual = hasht.contains('dog')
    expected = True
    assert actual == expected

def test_contains_false():
    hasht = Hashtable()
    hasht.set('dog', 'kaysee')
    actual = hasht.contains('cat')
    expected = False
    assert actual == expected

def test_keys():
    hasht = Hashtable()
    hasht.set('dog', 'kaysee')
    actual = hasht.keys()
    expected = 'dog'
    assert actual == expected 


