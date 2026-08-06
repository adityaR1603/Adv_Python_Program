class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"₹{amount} paid using Credit Card.")

class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"₹{amount} paid using Debit Card.")

class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"₹{amount} paid using UPI.")

class NetBankingPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"₹{amount} paid using Net Banking.")

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)

# Main Program
amount = float(input("Enter Payment Amount: ₹"))

print("\nSelect Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. Net Banking")

choice = int(input("Enter your choice: "))

if choice == 1:
    payment = CreditCardPayment()
elif choice == 2:
    payment = DebitCardPayment()
elif choice == 3:
    payment = UPIPayment()
elif choice == 4:
    payment = NetBankingPayment()
else:
    print("Invalid choice!")
    exit()

processor = PaymentProcessor(payment)
processor.process_payment(amount)
