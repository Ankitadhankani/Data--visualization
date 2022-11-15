class no:
    def sum(self,a,b):
        add=a+b
        print(add)
class numbers(no):
    def division(self,x,y):
        div=x/y
        print(div) 
class NUMBERS(numbers):
    def multiplication(self,n,m):
        mul=(n*m)
        print(mul)
A=NUMBERS()
A.multiplication(1234,678)
A.division(4656,7900)
A.sum(45677,7990)    
