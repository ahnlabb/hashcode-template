import cPickle as pickle
from inspect import getsource
from functools import wraps
from util import mkdir


def cached(func):
    """ Decorate to use pickled cache
    """

    @wraps(func)
    def cached_func(*args, **kwargs):
        cachedir = "cache"
        pkl_file = "{}/{}.pkl".format(cachedir, func.__name__)
        try:
            with open(pkl_file, 'r') as f:
                cache = pickle.load(f)
                valid = cache['function'] == getsource(func)
        except IOError:
            valid = False

        if valid:
            return cache['result']

        mkdir('cache')
        cache = {
            'function': getsource(func),
            'result': func(*args, **kwargs),
            'args': args,
            'kwargs': kwargs
        }
        with open(pkl_file, 'w') as f:
            pickle.dump(cache, f)

        return cache['result']

    return cached_func


def identity(func):
    return func
