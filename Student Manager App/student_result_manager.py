Student = {}

while True:
    print("----Student Managemnet System-----")
    print("1. Create Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    Number = input("Enter the number :")

    if Number == "1":
        name = input("Enter the name :")
        marks = input("Enter the marks :")
        Student[name] = marks
        print(f"{name} Student is successfully added to the list")

    elif Number == "2":
        if not Student:
            print("Student Not Found")
        else:
            for name, marks in Student.items():
                print(name, marks)
            

    elif Number == "3":
        name = input("Enter the name of the student to check their marks")

        if name in Student:
            marks = Student[name]

            if marks >= "40":
                print("PASS")

            else:
                print("FAIL")

    elif Number == "4":
        print("Exiting ..........")
        break;

    else:
        print("Invalid Input")
        
        
        
            