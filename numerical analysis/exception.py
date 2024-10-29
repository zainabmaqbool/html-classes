def divide_by(a , b):
    return a/b
try:
    ans =  divide_by(34 , 0)
except Exception as elf:
    print("smth went wrong", elf)
    print(elf.__class__)




file = open('text.txt' , mode = 'r')
data = file.readline()
print(data)
file.close()


with open( 'text.txt' , 'w') as file:
    file.write("this is a old file")
    
with open( 'text.txt' , 'a') as file:
    file.writelines(["\n this is a old file"])
    

#map
menu = ["expresso" , "mocha" , "latte" , "capp" , "americano"]
def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee
filter_coffee = map(find_coffee , menu)
print(filter_coffee)
for x in filter_coffee:
    print(x=