name= input("Enter your name please:")
age= float(input("Enter you age please :"))
gpa= float(input("Enter your gpa( please gpa must be between 0 and 5 ):"))
field_of_interest=input("Give us the Field of Interest : ")
Graduated=input("are you Graduated?(please answer only by yes or no):")

print("name:",name)
print("age:",age)
print("gpa:",gpa)
print("field of interest:",field_of_interest)
print("graduated:",Graduated)
if (age<25 and gpa>=3.5 and Graduated.lower() =="yes"):
    print("the user is eligible for a scholarship.")
elif(age<30 and gpa>=2.5 ):
    print("the user is eligible for an internship.")
else:
    print("please apply again later.")
