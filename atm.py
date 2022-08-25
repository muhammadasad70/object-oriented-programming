class Atm:
    def __init__(self,acc_num,name,age,ph_num,cnic):
        self.acc_num=acc_num
        self.name=name
        self.age=age
        self.ph_num=ph_num
        self.cnic=cnic
print("customer_1 enter your details")
customer_1=Atm(eval(input("enter account number")),input("enter your name"),int(input("enter your age")),int(input("enter your ph num"))
               ,eval(input("enter your cnic")))
print("customer_2 enter your details")
customer_2=Atm(eval(input("enter account number")),input("enter your name"),int(input("enter your age")),int(input("enter your ph num"))
               ,eval(input("enter your cnic")))
print(customer_1.name)


