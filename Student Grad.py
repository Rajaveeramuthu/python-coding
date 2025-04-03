mark = int(input("Enter the student Mark: "))

if mark < 45:
    print("RA")
elif 45 <= mark <= 50:
    print("C")
elif 51 <= mark <= 60:
    print("B")
elif 61 <= mark <= 70:
    print("B+")
elif 71 <= mark <= 80:
    print("A")
elif 81 <= mark <= 90:
    print("A+")
elif 91 <= mark <= 100:
    print("O")
else:
    print("Invalid mark")  
