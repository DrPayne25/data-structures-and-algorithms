def hash_left_join(left_hash, right_hash):
    combined_hash = []

    for key in left_hash:
        combined_hash.append(key)
        combined_hash.append(left_hash[key])

        if key in right_hash:
            combined_hash.append(right_hash[key])
        else:
            combined_hash.append(None)
    return combined_hash
