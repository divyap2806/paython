'''write a program to check if a number is a single digit number, 2-digit number and so on .... up to 5 digit

num = int(input("enter a number up to 5 digit : "))

if num <= 9 :
    print("number is single digit")
elif (num >= 10)and (num <= 99) :
    print("number is two digit")
elif num >= 100 and num<= 999 :
    print("number have three digit")
elif num >= 1000 and num <= 9999 :
    print("number have four digit")
elif num >= 10000 :
    print("number have five digit")

else:
    print("number is invalid")'''






'''write a program check whether the passed letter is a vowel or not

letter = input("enter a letter :")
print(letter)
if letter == 'a ' or letter == 'e' or letter == 'i' or letter == 'o' or letter== 'u'  :
    print("letter is vowel")

else:
    print("letter is not a vowel")'''

'''#method 2
if letter in "aeiou" or "AEIOU" :
   print("letter is vowel")
else:
    print("not vowel")'''



#write a program to create area calculator

'''print("*******AREA CALCULATOR********"\n)

print(""" press 1 to get the area of squre
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get the area of triangle""")

choice = int(input("enter your choice : "))
print(choice)

if choice == 1:
    side = float(input("enter the lenghth of the sqare"))
    area = side**2
    print("area of sqare:" , area)

elif choice ==2:
    radius = int(input("enter the radius of circle"))
    area = 3.12*radius*radius
    print("area of circle:" ,area)

elif choice ==3:
    length = float(input("enter the leght of rectangle"))
    width = float(input("enter the width of rectangle"))
    area = length * width
    print("area of rectangle : :" ,area)

elif choice ==4:
     base= float(input("enter the base  of  tirangle"))
     height= float(input("enter the height of "))
     area = 1/2 *base*height
     print("area  of triangle :" ,area)

else:
    print("invalid input")'''



#write a program to chek given number is even or odd
'''
num = int(input("enter a number :"))

if num%2==0:
    print("number is even")
else:
    print("number is odd")
     '''



#write a program to chek given number is positive or not
'''
num = int(input("enter a number : "))
print(num)

if num >= 0 :
    print(" number is positive")

else:
    print("number is negative")'''



#write a program to tack details from a student for id card and then print it in diffrent lines.
'''name = (input("enter your name :"))
age = int(input("enter your age :"))
address = input("enter your address")
class_room= input("enter your class")
blood_group = input("enter your blood group")

print(name,age,address,class_room,blood_group,sep = "\n")'''


#write a code for convert float into integers
'''
height = float(input("enter :"))
print(height)
print(type(height))

height = int(height)
print(height)
print(type(height))
'''

#write a program to swap 2 variables

'''
a = 21
b= 32

print("a : " ,a)
print("b  : ",b )

temp = a
a = b
b = temp

print("a : ", a)
print("b  : ",b )

#method 2
a=38
b=30
print("a : " ,a)
print("b  : ",b )
a,b=b,a
print("a : " ,a)
print("b  : ",b )

'''

#write a program to display a persons name,age and address in three diffrent lines
'''
name = input("enter your name :")
age = int(input("enter your age :"))
address= input(" enter your address : ")
print(name,"\n", age,"\n" , address,"\n")
#print(name , age, address,sep = "\t")  in this we also use sep for the \n : , \t  etc....'''



'''
#user input
#defult it has a string datatype
name = input("enter your name : ")
print(name)

#integer input
age = int(input("enter age : "))
print(age)

#float input
height = float(input("enter your height"))
print(height)

#evalute input
exp1 = eval(input("enter any expression"))
print(exp1)
'''


'''#table of any number
n = int(input("enter any number : "))
for i in range(1 ,11):
    table = n*i
    print(n,"x" ,i ,"=",table)

#method 2
n = int(input("enter any number : "))
i = 1
while i <=10:
    print(n,"x",i,"=" , n*i)
    i+=1

'''

'''
#true while loop
while True:
    num1 = int(input("enter num1 : "))
    num2 = int(input("enter num2 : "))
    print(num1 +num2)

    repeat = input("do you want to stop the program :  ")
    
    if repeat == "yes":
        break'''

'''pattern making
#method 1
for i in range(1,6):
    for j in range(1,i+1):
        print("*" , end = " ")
    print()

#method 2
for i in range(1,6):
    print("* " *i)

#method 3
i=1
while i<=5:
    print("*" * i)
    i+=1'''

