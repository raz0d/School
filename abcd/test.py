import pickle
def disp_Detail():
f=open("emp.dat","wb")
ans="y"
while ans=="y":
    emp_id=int(input("enter emp_id"))
    name=input("enter name")
    salary=int(input("enter salary"))
    list=[emp_id,name,salary]x