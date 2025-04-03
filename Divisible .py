number = int(input("Enter the Number"))

if ( number%3==0 and number%5==0):
    print("devisible by 3 and 5")
elif (number%3==0):
    print("devisible by 3")
elif(number%5==0):
    print ("it only devisible by 5")
else:
    print("not divisible by 3 and 5")
