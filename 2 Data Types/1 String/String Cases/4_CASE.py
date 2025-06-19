# NUMBER FORMATTING WITH ALIGNMENT
# <, >, ^ and = are used for alignment
# <= = >Left Alignment to the remaining space
# ^= == >Center alignment to the remaining space
# >= == > Right alignment to the remaining space
# = == = > Forces the signed(+)(-) to the left most position

# Note: Default Alignment for numbers is Right Alignment

print("{:5d}".format(12))
print("{:<5d}".format(12))
print("{:<05d}".format(12))
print("{:>5d}".format(12))
print("{:>05d}".format(12))
print("{:^5d}".format(12))
print("{:=5d}".format(12))

print("{:^10.3f}".format(12.23456))
print("{:=8.3f}".format(-12.23456))
