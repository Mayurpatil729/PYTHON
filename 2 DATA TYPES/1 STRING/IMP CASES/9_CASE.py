
# Dynamic formatting using format()

string = "{:{fill}{align}{width}}"
print(string.format('cat', fill='*', align='^', width=5))
print(string.format('cat', fill = '*', align = '^', width = 6))
print(string.format('cat', fill='*', align='<', width=6))
print(string.format('cat', fill='*', align='>', width=6))


# Dynamic float format template
print()

num = "{:{align}{width}.{precision}f}"
print(num.format(123.236, align='<', width=8, precision=2))
print(num.format(123.236, align = '>', width = 8, precision = 2))








