def calculate_electricity_bill(units, rate_per_unit, tax_percentage):
    bill_amount = units * rate_per_unit
    tax_amount = (tax_percentage / 100) * bill_amount
    total_bill = bill_amount + tax_amount
    return total_bill

units_consumed = 650
rate = 16.48
tax = 7.5

bill = calculate_electricity_bill(units_consumed, rate, tax)
print("Total total electricity bill is:", round(bill, 2))
