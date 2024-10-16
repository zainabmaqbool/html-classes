#switch statement
#obtainmarks = input("enter the marks")
#totalmarks = 100
#percentage= float(obtainmarks)/float(totalmarks)*100
#atch percentage:
    #case >85 or = 100:
        #print("A")
    #case  > 80 or = 85:
        #print("B")
    #case > 75 or =80 :
        #print("C")
    #case > 65 and =75:
         #print("D")
    #case >55 and =65:
         #print("E")
    #case _:
         #print("F")
#for loop
# favourite= ['creme brulee', 'apple pie', 'churros', 'toffee']
# for desert in favourite:
#     print('one of my favourite desert is', desert)
#while loop
favourite= ['creme brulee', 'apple pie', 'churros', 'toffee']
count = 0
while count<len(favourite):
    print('one of my favourite desert is', favourite[count])
    count +=1
#bubble sort
def bubble_sort(arr):

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
# Sample list to be sorted
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(arr)
bubble_sort(arr)
print("Sorted list is:")
print(arr)


