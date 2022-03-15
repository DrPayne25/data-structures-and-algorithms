from code_challenges.hash.hashtable import Hashtable

def hashmap_repeated_word(text):
    word_accumulator = ""
    hashmap = Hashtable()
    for char in text:
        lower_char = char.lower()
        if ord(lower_char) in range(ord("a"), ord("z")+1):
            word_accumulator += lower_char
        elif len(word_accumulator):
                if hashmap.contains(word_accumulator):
                    return word_accumulator
                else:
                    hashmap.set(word_accumulator, None)
                    word_accumulator = ""
    if len(word_accumulator) and hashmap.contains(word_accumulator):
        return word_accumulator
    return None
