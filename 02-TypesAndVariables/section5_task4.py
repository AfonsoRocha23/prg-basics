###
# A program that calculates 23% VAT from a given amount.
#
amount_str = input('Enter amount: ')
amount = float(amount_str)
vat = amount * 0.23

print(f'Amount  : {amount:.2f}')
print(f'VAT 23% : {vat:.2f}')
