# **Python Programming Assignment: Number Exploration Tool**
## Empty List

Num[]

## Take input user Name

name=input("Enter your name:")

## Take input favourite No.

### First favourite No.

num1=int(input("Enter your first favorite number:"))

### Second favourite No.

num2=int(input("Enter your first favorite number:"))

### Third favourite No.

num3=int(input("Enter your first favorite number:"))

## Numbers stored in a List

num.extend(num1, num2, num3)

## Greet the user with a personalized message

print(f"Hello,{name}!, Let's explore your favorite numbers:")

## Add number in a list

num.extend([num1,num2,num3])

## Check Even or odd No. in a List

### Check First favourit No.

if (num[0] % 2) == 0:

   print("The number {0} is Even.".format(num[0]))
   
else:

   print("The number {0} is Odd.".format(num[0]))

### Check Second favourit No.   
   
if (num[1] % 2) == 0:

   print("The number {0} is Even.".format(num[1]))
   
else:

   print("The number {0} is Odd.".format(num[1]))

### Check Third favourit No.

if (num[2] % 2) == 0:

   print("The number {0} is Even.".format(num[2]))
   
else:

   print("The number {0} is Odd.".format(num[2]))

## Save numbers in tuple   

### Save Whole list

tup=(num)

#### Save First favourit No.

tup1=(num[0])

#### Save Second favourit No.

tup2=(num[1])

#### Save Third favourit No.

tup3=(num[2])

## Find square of Nos.

print("The number", tup1,"and its square:", (tup1, tup1*tup1))

print("The number", tup2,"and its square:", (tup2, tup2*tup2))

print("The number", tup3,"and its square:", (tup3, tup3*tup3))

## Sum of three Nos

sum=sum(tup)

print("\n""Amazing! The sum of your favorite numbers is:",sum)

## Find sum of nos. is prime no or not

if sum > 1:

   for i in range(2,sum):
   
       if (sum % i) == 0:
       
### Notify the user with an appropriate message.

           print(sum,"is not a prime number.")
           
           break
           
   else:
   
       print("Wow",sum,"is a prime number!")

## **End**
