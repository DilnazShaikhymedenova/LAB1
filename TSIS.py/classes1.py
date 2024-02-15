class my_class:
    def getString(a):
        a = str(input())
        return a
    def printString(self,c):
        print(c.upper())
p1 = my_class()
b = p1.getString()
p1.printString(b)
# getString() - method takes user input and stores in input_string
#printString() - method to print the stored string in upper case letter 