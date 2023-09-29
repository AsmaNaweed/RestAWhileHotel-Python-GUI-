import LoginModule
print ("hello python");
def my_function():
  print("Hello from a function")
my_function();

LoginModule.AddLogin("iffi", "1234")
loginSuccess = LoginModule.VerifyLogin("iffi", "1234" )

if loginSuccess == True:
  print("Your username and password is valid");
else:
  print("your username password is not valid");


