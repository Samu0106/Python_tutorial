a= int(input("Enter your age: "))

# if statement 1:
if(a%2==0):
    print("a is even")
# end of if statement 1

# both if are independent of it's owm; 

# if statement 2:
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
# end if statement 2
print("End of program")