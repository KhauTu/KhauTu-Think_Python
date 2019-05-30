import time
'''
time.clock has been deprecated in Python 3.3 and 
will be removed from Python 3.8: use time.perf_counter or time.process_time instead
'''
def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

sz = 10000000 # Lets have 10 million elements in the list
testdata = range(sz)

t0 = time.process_time()
my_result = do_my_sum(testdata)
t1 = time.process_time()
print("my_result = {0} (time taken = {1:.4f} seconds)".format(my_result, t1-t0))

t2 = time.process_time()
their_result = sum(testdata)
t3 = time.process_time()
print("their_result = {0} (time taken = {1:.4f} seconds)".format(their_result, t3-t2))