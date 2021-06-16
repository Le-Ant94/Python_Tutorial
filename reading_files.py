employee_files = open("employees.txt", "r") #reading from employees.txt file
#r stands for "read", w stands for "write", a stands for "append"-add more info but can't change, r+ stands for read and write

for employee in employee_files.readlines():
    print(employee)

print(employee_files.readline())
print(employee_files.readline())

employee_files.close()
