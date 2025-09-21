""" 
基于生成器的上下文管理器
"""
import contextlib
import sys

@contextlib.contextmanager
def looking_glass():
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
        
    sys.stdout.write = reverse_write

    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


@looking_glass()
def verse():
    print('The time has come')

verse()

print('back to normal')