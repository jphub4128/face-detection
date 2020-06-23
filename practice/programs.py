
n=input("enter the number")
n1=int(n)
if n1%2==1:
 print("wierd")
elif n1%2==0 and 2<n1<=5:
 print("not wierd")
elif n1%2==0 and 6<n1<=20:
 print("wierd")
else:
 print("not wierd")
