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