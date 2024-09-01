num = []
name=input("Enter your name:")
num1=int(input("Enter your first favorite number:"))
num.append(num1)
num2=int(input("Enter your second favorite number:"))
num.append(num2)
num3=int(input("Enter your third favorite number:"))
num.append(num3)
print(f"Hello,{name}!, Let's explore your favorite numbers:")
if (num1 % 2) == 0:
   print("The number {0} is Even".format(num1))
else:
   print("The number {0} is Odd".format(num1))

if (num2 % 2) == 0:
   print("The number {0} is Even".format(num2))
else:
   print("The number {0} is Odd".format(num2))

if (num3 % 2) == 0:
   print("The number {0} is Even".format(num3))
else:
   print("The number {0} is Odd".format(num3))

sum=0
for ele in range(0, len(num)):
   sum=sum+num[ele]
print("Amazing! The sum of your favorite numbers is:", sum)

if sum > 1:

   for i in range(2,sum):
       if (sum % i) == 0:
           print(sum,"is not a prime number.")
           break
   else:
       print("Wow",sum,"is a prime number!")