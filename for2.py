lst = [5,(1,2,3),{'abc','xyz'}]
for k in lst:
    print(k)

# Cú pháp comprehension:
# [ output-expression for-statement optional-predicate ]

# Phép toán dịch bit

print(['--'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('how', 'kteam', 'EDUCATION'), ('chia', 'sẻ', 'FREE')]]) # bỏ trống optional-predicate

print({key:value + 1 for key, value in (('Kteam', 69), ('Tèo', 50), ('Tũn', 14), ('Free Education', 93)) if value % 2 != 0})
