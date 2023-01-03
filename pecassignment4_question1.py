# grades according the marks input   
marks = int(input("Enter your marks : "))
if marks<25:
    print("F")
elif 25<=marks<45:
    print("E")
elif 45<=marks<50:
    print("D")
elif 50<=marks<60:
    print("C")
elif 60<=marks<=80:
    print("B")
elif 80<marks<=100:
    print("A")
else :
    print("please enter your correct marks")