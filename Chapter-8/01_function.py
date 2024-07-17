# A function is a group of statements performing a specific task
# suppose we want to average of number

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))

avg=a+b+c/3
print(avg)
#If we want the average multiple time like 5 times we can copy but if we want 50 times we use function as

#function defination:
def avg():

    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    c=int(input("Enter the number: "))

    avg=a+b+c/3
avg() # calling the function
# if we want to call function more time we can do this as below
avg()
avg()
avg()
# or we can create loop so that function execute multiple times