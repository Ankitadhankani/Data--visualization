class billing:
    def __init(self):
        print("welcome to our shope")
    def bill(self,amt):
        discount=amt*9/100
        bill=amt-discount
        print(discount)
        print(bill)
o=billing()
o.bill(30000) 
#constructor overloading is not alow in python.
# construtor is an special function of classthan runs automatically when it calls.
           
