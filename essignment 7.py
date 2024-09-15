num = []
name=input("Enter your name:")
num1=int(input("Enter your first favorite number:"))
num2=int(input("Enter your second favorite number:"))
num3=int(input("Enter your third favorite number:"))

print("\n"f"Hello, {name}! Let's explore your favorite numbers:")
num.extend([num1,num2,num3])
if (num[0] % 2) == 0:
   print("The number {0} is Even.".format(num[0]))
else:
   print("The number {0} is Odd.".format(num[0]))
if (num[1] % 2) == 0:
   print("The number {0} is Even.".format(num[1]))
else:
   print("The number {0} is Odd.".format(num[1]))

if (num[2] % 2) == 0:
   print("The number {0} is Even.".format(num[2]))
else:
   print("The number {0} is Odd.".format(num[2]))
tup=(num)
tup1=(num[0])
tup2=(num[1])
tup3=(num[2])
print("The number", tup1,"and its square:", (tup1, tup1*tup1))
print("The number", tup2,"and its square:", (tup2, tup2*tup2))
print("The number", tup3,"and its square:", (tup3, tup3*tup3))
sum=sum(tup)
print("\n""Amazing! The sum of your favorite numbers is:",sum)

if sum > 1:

   for i in range(2,sum):
       if (sum % i) == 0:
           print(sum,"is not a prime number.")
           break
   else:
       print("Wow",sum,"is a prime number!")