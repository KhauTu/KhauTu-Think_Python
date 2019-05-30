import math

x = 4.
y = 10

print(x*y)

pi = math.pi

r = 5

sphere = 4.0/3*pi*r**3

print('sphere with radius 5 has volume of ' + str(sphere))

# cover price of a book is $24.95
# discount 40%
# Shipping cost $3 for first copy; 75 cent for each additional copy

total_sale = 24.95 * (1.0 - 0.40) * 60 + 3 + 0.75 * (60 - 1)
print(total_sale)

cover_price = 24.95

number_of_books = int(input('How many books do you want to orderorder at wholesale?'))

def ship_cost(number_of_books):
    if number_of_books == 1:
        return(number_of_books * 3) # Cost of shipping one book is $3
    else:
        return(3 + (number_of_books -1) * 0.75) # Each additional copy of the book is $0.75 to ship

def wholesale_cost(number_of_books):
    return((cover_price * (1.0 - 0.4) * number_of_books) + ship_cost(number_of_books)) # There is a 40% discount on wholesale book sales

print('The cost of buying and shipping ' + str(number_of_books) + ' books is $' + str(round(wholesale_cost(number_of_books), 2)))

time_run = (8.0 + 15.0/60)*2 + (7.0 + 12.0/60)*3

time_home = 6 + (52 + time_run)/60
time_home_hr = int(time_home)
time_home_min = (time_home - time_home_hr)*60
print(time_run)
print('Finish time was %d:%d' %(time_home_hr, time_home_min))