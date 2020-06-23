leap=int(input("enter the year"))
def is_leap(l):
    if l%400==0:
        return True
    if l%100==0:
        return False
    if l%4==0:
        return True
    return False
print (is_leap(leap))
