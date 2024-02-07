def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Toibas", lname = "Refsnes")
#if the number of keyword arguments is unkniwn, add a double ** before the parameter name



def my_function(country = "Norway"):
    print("I am from" + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#default parameter value
#if we call the function without argument, it uses the default value


