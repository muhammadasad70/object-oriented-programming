class EvenNUmber:
    def __init__(self,num):
        if num%2==0:
            print("this is even number")
        else:
            print("this is odd number")
            self.num = num
number=EvenNUmber(int(input("enter a number")))
print(number)





