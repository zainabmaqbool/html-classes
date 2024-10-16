# Nested loop
# for loop syntax (for x in range(10):)
for x in range(10):#yeh range show karega 0 to 10
    print(x)#part of outer loop
    for y in range(2):#yeh range k anadar itne time yeh text show karega
        print("hi")
#swapping
x = 10;
y = 30;
print(x)
print(y)
temp = x;
x = y;
y = temp;
print("x", x)
print("y", y)
#bubble sort
# Bubble sort in Python

def bubbleSort(array):
  # loop to access each array element
  for i in range(len(array)):
    # loop to compare array elements
    for j in range( len(array)- 1):
      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:
        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
data = [3, 45, 52, 11, 23]
bubbleSort(data)  
print('Sorted Array in Ascending Order:')
print(data)

array=[20,45,33,12,34]
for i in range(len(array)-1,0,-1):#yahn 0 index to show karega or -1 mirror k liye
    for j in range(i):#i=4 or phir -1 karege or j=0 hoga
        if array[j]> array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
bubbleSort(array)
print('After Sorting 2:')
print(array)
#electricity bills
def calculate_electricity_bill(units, rate_per_unit, tax_percentage):
    """
    Function to calculate electricity bill with tax.
    
    Args:
    units (float): The total number of units consumed.
    rate_per_unit (float): The rate per unit of electricity.
    tax_percentage (float): The tax percentage to be applied on the bill (in %).
    
    Returns:
    float: The total electricity bill amount including tax.
    """
    bill_amount = units * rate_per_unit
    tax_amount = (tax_percentage / 100) * bill_amount
    total_bill = bill_amount + tax_amount
    return total_bill

# Example usage:
units_consumed = 350  # Replace with actual units consumed
rate = 0.15  # Replace with actual rate per unit in your currency
tax = 10  # Tax percentage (e.g., 10%)

bill = calculate_electricity_bill(units_consumed, rate, tax)
print(f"Your total electricity bill, including tax, is: {bill:.2f}")
