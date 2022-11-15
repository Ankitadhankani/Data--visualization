class employee:
    def __init__(self):
        print("welceom to our office") 
    def tax(self,salary):
        if salary>=50000:
            tax=salary*3/100
        else:
            tax=0  
        print("tax",tax)      
a=employee()
a.tax(600006)
