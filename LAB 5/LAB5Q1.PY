empDetails=[]

def empGetter(id,name,sal,dept):
    empDetails.append((id,name,sal,dept))

def search(id):
    for emp in empDetails:
        print(emp[0])
        if emp[0]==id:
            return emp
        else:
            return "emp not found"


if __name__== "__main__":
    n = int(input("Enter number of emp"))

    while n>0:
        print("Enter details of the details of emp:")
        print("Enter Id:")
        id=input()
        print("Enter Name:")
        nm = input()
        print("Enter Salary:")
        sal=input()
        print("Enter Dept:")
        dept = input()
        empGetter(id,nm,sal,dept)
        n=n-1
    print("Enter the id of the employ to be searched:")
    id = input()
    print("Details : " + str(search(id)))
    


