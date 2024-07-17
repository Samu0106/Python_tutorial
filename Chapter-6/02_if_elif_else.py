#if elif else ladder

a= int(input("Enter your age: "))

if(a>18):  # the space after we enter in if is indentation
    print("You are above the age of consent")
    print("Good for you")
#for if user enter negative age we can add condition elif 
elif(a<0):
    print("Entered invalid age")
elif(a==0):
    print("your are entering zero which is a invalid age")
else:
    print("You are below the age of consent")

print("End of program")