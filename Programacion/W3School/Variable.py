x = 5 #INT
y = "John" #STR
Z = 5.4 #FLOAT

a = 3
str(a) #str "3"
int(a) #int 3
float(a) #float 3.0

type(a) #te dice el tipo de variable

x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"

fruits = ["Orange", "Banana", "Cherry"]
x, y, z = fruits

#Global variables
x = "awesome"
def myfunc():
    print("Python is " + x)#PYTHON IS AWASOME
myfunc()

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x) #python is fantastic
myfunc()
print("Python is " + x) #python is awasome

def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x) #python is dantastic

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x) #python is fantastic
