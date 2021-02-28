import collections

my_counter = collections.Counter()

def log_and_count(key=None, counts=my_counter):
    def wrapper_function(original_function):
        def inner_function(*args, **kwargs):
            if key:
                counts[key] += 1
            else:
                counts[original_function.__name__] += 1
            print('called {} with {} and {}'.format(original_function.__name__, args, kwargs))
            return original_function(*args, **kwargs)
        return inner_function
    return wrapper_function

@log_and_count(key='basic functions', counts=my_counter)
def f1(a, b=2):
    """ test na f1
    >>>f1(2)
    'called f1 with (2,) and {}'
    >>> f1(a=2, b=4)
    'called f1 with () and {'a': 2, 'b': 4}'
    """
    return a ** b

@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
    """ test na f1
    >>>f2(2, b=4)
    'called f2 with (2,) and {'b': 4}'
    >>> f2(4)
    'called f2 with (4,) and {}'
    >>> f2(5)
    'called f2 with (5,) and {}'
    """
    return a ** 2 + b

@log_and_count(counts = my_counter)
def f3(a, b=5):
    """ test na f1
    >>>f3(5)
    'called f3 with (5,) and {}'
    >>> f3(5,4)
    'called f3 with (5, 4) and {}'
    
    """
    return a ** 3 - b
    
f1(2)
f2(2, b=4)
f1(a=2, b=4)
f2(4)
f2(5)
f3(5)
f3(5,4)
print(my_counter)
