API_KEY = "XKDhd-dkxD" # String Type
PORT = 8080  #Number type

username = "Finley"
fullname = "Finley Charles Jacob"
age = 25 
title = "Mr."
nationality = "Finland"


grocery_items = ["fruits", "vegetables", "Eggs", "Beacon and Cheese", "Beef", "Lettuce"] # Lists or Array

# Object
user = {
    username:username,
    fullname:fullname,
    age:age,
    title:title
}

#functions without parameter or return statement
def printUserName():
    print(username)

#function without parameter but with return statement
def getFullname():
    return fullname

def updateFullname():
    updatedName = "Finley Jacob"
    return updatedName

def getAge():
    return age


printUserName()
getFullname()
fullname = updateFullname()

getAge()


# Classwork 1
def userDateOfBirth(age):
    """
    Write a simple function that returns the dob from the age provided

    return 
    -------
    dob. e.g. 1984 or 1995. It should be a number value.
    """

# Class work 2: Function with parameter
def printFullname(fullname):
    """
    Write a simple function that prints the users' fullname it.
    """

printFullname(fullname=fullname)

#class work 3: Function with parameter and return statement
def firstName(fullname):
    """
    Write a function that returns only the first name of the fullname given, using text maninpulation

    Use: https://docs.python.org/3/tutorial/introduction.html#text

    Return
    ----------

    name String
    """