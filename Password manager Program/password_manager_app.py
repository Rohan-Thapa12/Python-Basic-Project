import random
import string

Password = {}

try:
    with open("example.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            Password[website] = pwd

except:
    pass

def gen_pass():
    char = string.ascii_letters + string.digits + "*&%$#@"
    password = "".join(random.choice(char) for _ in range(10))
    return password



while True:
    print("---Password Management App---")
    print("1.Save Password")
    print("2. View Password")
    print("3. Generate Passwoed")
    print("4. Exit")
    
    choice = input("Enter youre choice :")

    if choice == "1":
        website = input("Enter the website :")
        pwd = input("Enter the password :")
        Password[website] = pwd

        with open("example.txt", "a") as file:
            file.write(f"{website} : {pwd}\n")
        print(f"Youre {website} passwoed is saved")

    elif choice == "2":
        if not Password:
            print("Not Found")

        else:
            for website, pwd in Password.items():
                print(website, ":", Password)

    elif choice == "3":
        print("Youre generated passwors is :", gen_pass())
        print("Thank you for choosing our password generator")

    elif choice == "4":
        print("Exiting......................")
        break

    else:
        print("Invalide Input. Please choose a valid option.")
        
