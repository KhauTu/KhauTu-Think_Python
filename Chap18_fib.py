import time

def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t

t0 = time.perf_counter()
n = 35
result = fib(n)
t1 = time.perf_counter()

print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

import os

def get_dirlist(path):
    """
        Return a sorted list of all entries in path.
        This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "": # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "
    
    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f) # Print the line
        fullname = os.path.join(path, f) # Turn name into full pathname
        if os.path.isdir(fullname): # If a directory, recurse.
            print_files(fullname, prefix + "| ")
            