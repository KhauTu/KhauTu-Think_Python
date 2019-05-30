def num_digits(n):
    count = 0
    if n == 0:
        count += 1
    else:
        if n < 0:
            n = -n
        while n != 0:
            count = count + 1
            n = n // 10
    return count

def num_even_digits(n):
    count = 0
    if n == 0:
        count += 1
    else:
        if n < 0:
            n = -n
        while n != 0:
            check = n % 10
            if check % 2 == 0:
                count += 1
            n = (n - check) / 10
    return count

def sum_of_squares(xs):
    sum = 0
    for x in xs:
        sum = sum + x*x
    return sum

print(sum_of_squares([2, -3, 4]))
# print(num_even_digits(-10000))
# print(num_digits(-12345))