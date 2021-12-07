class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) / 100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products)-self.totalDiscount(products)
        return total_pure_price

    #   New function that determines the total quantity of all the items the user inputs.
    #   It then returns that amount, allowing for an easy function call in main to display it to the user.
    def totalQuantity(self, products):
        total_quantity = 0
        for k, v in products.items():
            total_quantity += int(v['qnt'])
        return total_quantity

    #   New function that determines the amount of money that will be discounted from the price of the product inputted.
    #   The function then returns the discount amount, allowing for an easy function call in main to display it to the user.
    #   This allows the user to see how much money is saved.
    def displayDiscountAmount(self, products):
        total_discount_value = 0
        for k, v in products.items():
            total_discount_value += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) / 100
        total_discount = round(total_discount_value, 2)
        return total_discount_value

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput
