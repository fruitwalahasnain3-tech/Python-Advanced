with open("student.txt","w") as file:
    file.write("Hasnain\n BCA\n ")

with open("student.txt","a") as file:
    file.write("Python\n Pandas")

with open("student.txt","r") as file:
    print(file.readlines())