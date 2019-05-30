my_tickets =    [[ 7, 17, 37, 19, 23, 43],
                [ 7, 2, 13, 41, 31, 43],
                [ 2, 5, 7, 11, 13, 17],
                [13, 17, 37, 19, 23, 43]]

def lotto_draw():
    '''a function to return a lotto draw (6 numbers) randomly (from 1 to 49).'''
    import random
    rng = random.Random()
    number_lst = list(range(1,49))
    rng.shuffle(number_lst)
    lotto = [number_lst[i] for i in range(6)]
    return lotto

def lotto_match(lotto, draw):
    '''a function that compares a single ticket and a draw,
    and returns the number of correct picks on that ticket'''
    match = 0
    for i in range(6):
        if draw[i] in lotto:
            match += 1
    return match

def lotto_matches(lotto, my_tickets):
    '''a function that takes a list of tickets and a draw,
    and returns a list telling how many picks were correct on each ticket'''
    matches = []
    for i in range(len(my_tickets)):
        k = lotto_match(lotto, my_tickets[i])
        # print(k)
        matches.append(k)
    return matches

def is_prime(n):
    '''function checking if a number is prime'''
    if n < 4:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 2
        while i * i <= n:
            for k in range(2,i+1):
                if n % k == 0:
                    return False
            i += 1
        return True

def primes_in(lst):
    '''a function that takes a list of integers,
    and returns the number of primes in the list:'''
    prime_num = 0
    for l in lst:
        if is_prime(l):
            prime_num += 1
    return prime_num

# print(lotto_match([42,4,7,11,1,13],[2,5,7,11,13,17]))
# print(lotto_matches([42,4,7,11,1,13], my_tickets))

# print(primes_in([42, 4, 7, 11, 1, 13]))

def prime_lower(n):
    '''function return a list of prime numbers lower than n'''
    prime_lower_lst = []
    for i in range(n):
        if is_prime(i):
            prime_lower_lst.append(i)
    return prime_lower_lst

def prime_miss(lst, lst_prime):
    '''function return a list of missed prime numbers,
    which appears in lst_prime, but not in lst'''
    # lst_prime = prime_lower(50)
    for v in lst:
        if v in lst_prime:
            index_v = lst_prime.index(v)
            lst_prime.pop(index_v)
    return lst_prime

def prime_misses(my_tickets):
    '''a function to discover whether 
    the computer scientist has missed any prime
    numbers in her selection of the four tickets.
    Return a list of all primes that she has missed'''
    int_lst_prime = prime_lower(50)
    lst_prime = [i for i in range(len(my_tickets))]
    lst_prime[0] = int_lst_prime
    i = 0
    while i + 1 < len(my_tickets):
        lst_prime[i+1] = prime_miss(my_tickets[i],lst_prime[i])
        i += 1
    return lst_prime[-1]

# print(is_prime(49))
# lst = prime_miss([42, 4, 7, 11, 1, 13])
# print(lst.index(41))

# print(prime_misses(my_tickets))
def ave_correct(num):
    # import random
    # rng = random.Random()
    tries = 0
    m = 20
    num_found = 0
    sum = 0
    while num_found < m:
        lotto = lotto_draw()
        # rng.shuffle(my_tickets)
        match = [0, 1, 2, 3]
        for i in range(4):
            match[i] = lotto_match(lotto, my_tickets[i])
        tries += 1
        if max(match) >= num:
            print("the {0} times. Found in {1} tries.".format(num_found+1, tries))
            num_found += 1
            sum += tries
            tries = 0
    ave = sum/num_found
    return ave

# print(ave_correct(4))