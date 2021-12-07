from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('What is your product : ')
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    repeat = Invoice().inputAnswer("Another  product? (y,n) : ")
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == "n":
        break

total_amount = Invoice().totalPurePrice(products)
total_discount_amount = Invoice().displayDiscountAmount(products)
total_quantity_amount = Invoice().totalQuantity(products)

print("Your total pure price is: ", total_amount)
print("Your total discount saved is: ", total_discount_amount)
print("Your total quantity selected is: ", total_quantity_amount)