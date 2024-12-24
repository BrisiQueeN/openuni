marks= float(input("enter the marks:"))
if 0 <= marks <=100:
    if marks>=85:
        print ("grade is A+")
    elif marks>=80:
        print("grade is A")
    elif marks>=75:
        print("grade is A-")
    elif marks>=70:
        print("grade is B+")
    elif marks>65:
         print("grade is B")
    elif marks>=60:
        print("grade is B-")
    elif marks>=55:
        print("grade is C+")
    elif marks>=50:
        print("grade is C")
    elif marks>=45:
        print("grade is C-")
    elif marks>=40:
        print("grade is S+")
    elif marks>=35:
        print("grade is S")
    elif marks>=30:
        print("grade is S-")
    else:
        print("unfortunatly you are week")
else:
    print("enter the vaild marks:")

