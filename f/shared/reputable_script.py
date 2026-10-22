# py: ==3.15.*
import sys
import platform


def main():

    print("Python version:", sys.version)
    print("Python executable:", sys.executable)
    print("Python implementation:", platform.python_implementation())
    print("Hello World")