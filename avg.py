sub1=int(input("enter sub1 marks:"))
sub2=int(input("enter sub2 marks:"))
sub3=int(input("enter sub3 marks:"))
sub4=int(input("enter sub4 marks:"))
sub5=int(input("enter sub5 marks:"))
sub6=int(input("enter sub6 marks:"))
n=6
total_gain=(sub1+sub2+sub3+sub4+sub5+sub6)
avg=(total_gain)/6
if (avg>=90):
    print("First Class")
elif (avg>=75):
    print("second class")
elif (avg>=50):
    print("third class")
elif (avg>=35):
    print("pass")
else:
    print("fail")
