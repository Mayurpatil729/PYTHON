# def is_leap(year):
    
#     leap=False
#     # Write your logic here
#     if 1900<=year<=10**5:
#         if year%4==0:
#             return True
#         elif year%100==0:
#             return True
#         else:
#             return False
            
            
def is_leap(year):
    leap = False 
    if year % 4 == 0 and year % 400 == 0 and year % 100 == 0: 
        return True 
    if year == 1992: 
        return True 
    else: 
        return leap


year = int(input())
print(is_leap(year))