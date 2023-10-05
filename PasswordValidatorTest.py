from LoginModule import PasswordValidator

def getting_input():
    print("About to construct object")
    validator = PasswordValidator()
    print("Object Constructed")
    password= "123456"
    while password != "":
        print("Enter a password to validate")
        password = input()
       
        if validator.is_valid(password):
            print("Password has been approved.")
           
    else:
            print("Not a valid password.")

getting_input()
