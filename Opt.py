import random

name=input("Enter Your username: ")

p=input("Do you want to a random password(y/n)?: ")

if p=='Y' or p=='y':

    otp = random.randint (100000, 999999)

    print("RANDOM PASSWORD is:", otp)

    print("YOUR USERNAME IS: ", name)

    print("YOUR PASSWORD IS: ",otp)

else:

    pswd=input("Enter your own password: ")

    print("YOUR USERNAME IS: ", name)
   
    print("YOUR PASSWORD IS: ",pswd)
