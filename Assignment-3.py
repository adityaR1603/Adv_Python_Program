# Strategy Classes

class CreditCard:

    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


class UPI:

    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")

class Payment:

    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# Using Credit Card
p = Payment(CreditCard())
p.make_payment(1000)

# Using UPI
p = Payment(UPI())
p.make_payment(500)