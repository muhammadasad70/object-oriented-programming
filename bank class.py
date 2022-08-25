class Employee:
    def __init__(self,fname,account,phone_number,cnic,lname):
        self.fname=fname
        self.lname=lname
        self.cnic=cnic
        self.account=account
        self.phone_number=phone_number

employee_1=Employee("Muhammad ","saving","03016996105","38405-5804162-3","Asad")
employee_2=Employee("Muhammad ","current","030469961344","38405-5804162-3","Ali")
employee_3=Employee("Muhammad ","default","03049010167","38405-5804162-3","Ahamd")
employee_4=Employee("Muhammad ","paying","03016846105","38405-5804162-3","Abdullah")
print(employee_1.fname)
