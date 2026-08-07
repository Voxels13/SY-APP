#A Program to implement a Configurable Payment Processing System Using Strategy Pattern


from abc import ABC, abstractmethod

#Here, PaymentStrategy will act as the blueprint for all pay() functions
#Forces all payment methods to include a 'pay' method (due to use of abstract method)

class PaymentStrategy(ABC): #We pass ABC here for code safety (Protects it from typos)
    @abstractmethod
    def pay(self,amount:float):  #NOTE, here doing amount:float just tells other developers that amount takes in a float ":float" itself does nothing
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self,amount:float):
        print(f"Price ${amount:.2f} has been paid via Credit Card!") #Here, we format the amount to .2f i.e, two floating point numbers after the decimal

class PayPalPayment(PaymentStrategy):
    def pay(self,amount:float):
        print(f"Price ${amount:.2f} has been paid via Paypal!")

class BitcointPayment(PaymentStrategy):
    def pay(self,amount:float):
        print(f"Price ${amount:.2f} has been paid via Bitcoin!")


class PaymentProcessor:

    def __init__(self,paymentstrategy):
        self.paymentstrategy = paymentstrategy #Here we specify CreditCardPayment/PayPalPayment/BitcoinPayment

    def checkout(self, amount):
        self.paymentstrategy.pay(amount) #Takes in paymentstrategy value from above (which refers to a class) and uses its pay method for mentioned amount

#NOTE, to make this user friendly, declare all class names in lowercase letters and .lower() user input


if __name__ == "__main__":

    #Starting payment with CreditCard

    cart1 = PaymentProcessor(CreditCardPayment())
    cart1.checkout(1500.2554)

    #NOTE, here doing PaymentProcessor(CreditCardPayment()) and PaymentProcessor(CreditCardPayment) is very different
    #PaymentProcessor(CreditCardPayment()) {correct one} creates an object which an immediately accept a value and call .pay()
    #PaymentProcessor(CreditCardPayment) {wrong one} passes the raw blueprint i.e, how to make the same pay() method inside PaymentProcessor and will result in a compilation error

    #Change payment strategy to PayPal

    cart1.paymentstrategy = PayPalPayment()
    cart1.checkout(50)

    #Change payment starategy to Bitcoin

    cart1.paymentstrategy = BitcointPayment()
    cart1.checkout(175.65)




#Why do we use the Abstract Method

#If any other dev tries to create a new payment method and forgets to add a "pay" method inside it, Python will crash with an error when the user tries to use it. 
#Hence it acts as a safety net , signifying that a required method is missing



#Slightly Improved Version

#Strategy Pattern

def finalcheck(checkoutamount):
    if checkoutamount != 0 and checkoutamount > 0:
        print(f"Remaining unpaid amount:\n{checkoutamount}\n")
    elif checkoutamount == 0:
        print("Purchase Complete!")
    else:
        print("You overpaid!\n")
        print(f"{abs(checkoutamount)} has been returned to your account")
    
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self,amount:float):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self,amount:float):
        print(f"Price ${amount:.2f} via CreditCard\n")


class PayPalPayment(PaymentStrategy):
    def pay(self,amount:float):
        print(f"Paid ${amount:.2f} via PayPal\n")

class BitcoinPayment(PaymentStrategy):
    def pay(self,amount:float):
        print(f"Paid ${amount:.2f} via Bitcoin\n")


class PaymentProcess():

    def __init__(self,paymentstrategy):
        self.paymentstrategy = paymentstrategy

    def checkout(self,amount):
        self.paymentstrategy.pay(amount)

#MAIN

checkoutamount = float(input("Enter checkout amount: "))
is_running = True
while is_running:

    print(f"----------------------------------\nCheckout Amount: {checkoutamount}")
    amount1 = float(input("Enter amount to be paid via Credit Card\n:"))

    cart = PaymentProcess(PayPalPayment())
    cart.checkout(amount1)
    checkoutamount -= amount1

    finalcheck(checkoutamount)

    #Change Strategy


    if checkoutamount != 0 and checkoutamount >0:

        amount2 = float(input("How much would you like to pay via PayPal\n:"))
        cart.paymentstrategy = CreditCardPayment()
        cart.checkout(amount2)
        checkoutamount -= amount2

        finalcheck(checkoutamount)

    else:
        break

    #Change Strategy again
    if checkoutamount != 0 and checkoutamount >0:
        amount3 = float(input("How much would you like to pay via Bitcoin\n:"))
        cart.paymentstrategy = BitcoinPayment()
        cart.checkout(amount3)
        checkoutamount -= amount3

        finalcheck(checkoutamount)

    else:
        break

    is_running = False
