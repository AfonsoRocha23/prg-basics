###
# A program that calculates the product price after a discount.
#
price = float(input('Enter price: '))
discount_percent = float(input('Enter discount %: '))

# Calculations
discount_amount = price * (discount_percent / 100)
final_price = price - discount_amount

# Printing results with two decimal places
print(f'Product price: {price:.2f}')
print(f'Discount: {discount_percent}%')
print(f'Price with discount: {final_price:.2f}')
print(f'Reduction: {discount_amount:.2f}')
