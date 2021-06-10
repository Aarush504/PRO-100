class Atm(object):

        def __init__(self,card_number,pin):
            self.card_number = card_number
            self.pin = pin
                
        def wth(self):
            print("Money withdrawn...")
        
        def statement(self):
            print("Account statement:-")
            print("Sorry you dont have any money in your account...")

atm = Atm(21212121,1223)
print(atm.wth())
print(atm.statement())
        
