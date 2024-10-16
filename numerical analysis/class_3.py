list = [1,"Hello", 2.5, True]
print(type (list))
example_list = (1,"hello" , 4.5, True)
print(type(example_list))

print(len ("Hello world "))
#implicit
count =  12;
print (count)
count = 12.75
print(count)
count =  "hello";
print (count)
count = 13.75
print(count)
#explicity casting
count2 = 12;
print(type(str(count2)))
#user input
num1 = input("enter num1")
num2 = input("enter num2")
print (int(num1)+int(num2))
#user input sub
firstnum = input("enter firstnum")
secondnum = input("enter secondnum")
print (float(firstnum)-float(secondnum))

variable1 = 10
variable2 = 20
variable3 = 30
variable4 = 40
variable5 = 50
if variable1 >= variable2:
    print("variable1 is greater than variable2")
elif variable3 >= variable4:
    print("variable3 is greater than variable4")
else :
     print("variable4 is greater than variable5")
#mark sheet
obtainmarks = input("enter the marks")
totalmarks = 100
percentage= float(obtainmarks)/float(totalmarks)*100
if percentage>=85:
    print("A")
elif percentage>=80 and percentage<85:
    print("B")
elif percentage>=75 and percentage<80:
     print("C")
elif percentage>=65 and percentage<75:
     print("D")
elif percentage>=55 and percentage<65:
     print("E") 
else:
    print("F")    

