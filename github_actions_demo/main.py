import os,sys  # Bad import style
import math  # Unused import

def bad_function( x,y ):  # Bad spacing
    """This function has bad formatting"""
    z=x+y  # Bad spacing
    return z

def unused_function():
    pass

if __name__ == "__main__":
    result = bad_function(1,2)
    print(result) 