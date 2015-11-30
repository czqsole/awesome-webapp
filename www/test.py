# -*- coding: utf-8 -*-
__author__ = 'czq'
import functools

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func
        return  wrapper
    return decorator
@log
def now():
    print(now.__name__)
    print('2015-10-09')
now() # now = log(now)
# now()
@log2('execute')
def now2():
    print(now.__name__)
    print('2015-10-09')
now2() # now2 = log2('execute')(now2), log2('execute')返回decorator，decorator调用now2
