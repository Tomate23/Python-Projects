#Python Functions
"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
"""
#Creating a Function

def my_function(): #In Python a function is defined using the def keyword:
  print("Hello from a function")

#Calling a Function
#To call a function, use the function name followed by parenthesis:
  
def my_function():
  print("Hello from a function")
my_function() #like this

#Arguments
"""
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
"""
def my_function(fname): #the argument is named fname
  print(fname + " Refsnes")

my_function("Emil") #when we return our function with a value it's like thats the value of the argument
my_function("Tobias")
my_function("Linus")

#Number of Arguments
"""
By default, a function must be called with the correct number of arguments.
Meaning that if your function expects 2 arguments,
you have to call the function with 2 arguments, not more, and not less.
"""
#This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Return Values
"To let a function return a value, use the return statement:"
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))












