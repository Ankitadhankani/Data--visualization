#inheritance 
#single inharitance:consist one base or parent class class and one derive class child class
class no:
    def sum(self,a,b):
        add=a+b
        print(add)
class numbers(no):
    def division(self,n,m):
        div=n/m
        print(div) 
x=numbers()
x.division(2345,7899)
x.sum(678,890)              