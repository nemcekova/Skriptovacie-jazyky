def first_with_given_key(iterable, key=lambda x : x):
    new_keys = []
    it = iter(iterable)
    while True:
        try:
            value = next(it)
            if key(value) not in new_keys:
                yield value
                new_keys.append(key(value))
        except StopIteration:
            break
