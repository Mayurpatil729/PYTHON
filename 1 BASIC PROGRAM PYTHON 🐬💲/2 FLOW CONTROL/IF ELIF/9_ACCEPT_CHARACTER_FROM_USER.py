ch = (input("Enter any character = "))

if ch >= 'A' and ch <= 'Z':
    print("\n\t Capital Alphabet")
elif ch >= 'a' and ch <= 'z':
    print("\n\t Small alphabet ")
elif ch >= '0' and ch <= '9':
    print("\n\t Digits ")
else:
    print("\n\t Special symbols")
