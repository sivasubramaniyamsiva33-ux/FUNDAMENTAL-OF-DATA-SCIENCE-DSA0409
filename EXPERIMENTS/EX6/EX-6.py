"""
Exercise 6: Total Grocery Cost with Discount and Tax
Key Idea: iterate through items using zip(), apply discount and tax rates sequentially.
"""

prices = [100, 50, 200]
quantities = [2, 3, 1]
discount_rate = 10
tax_rate = 5

subtotal = 0
for price, quantity in zip(prices, quantities):
    subtotal += price * quantity

discount = subtotal * discount_rate / 100
after_discount = subtotal - discount
tax = after_discount * tax_rate / 100
total = after_discount + tax

print("Subtotal =", subtotal)
print("Discount =", discount)
print("Tax =", tax)
print("Total cost =", total)
