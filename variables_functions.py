API_KEY = "XKDhd-dkxD"
PORT = "8080"

username = "Finley"
fullname = "Finley Charles Jacob"
age = 25
title = "Mr."
nationality = "Finland"


grocery_items = ["fruits", "vegetables", "Eggs", "Beacon and Cheese", "Beef", "Lettuce"]

# Object
user = {
    username:username,
    fullname:fullname,
    age:age,
    title:title
}

def printUserName():
    print(username)

def getFullname():
    return fullname

def updateFullname():
    updatedName = "Finley Jacob"
    return updatedName

def getAge():
    return age

def userDateOfBirth(age):
    """
    Write a simple function that returns the dob from the age provided

    return 
    -------
    dob. e.g. 1984 or 1995. It should be a number value.
    """
def printFullname(fullname):
    """
    Write a simple function that prints the users' fullname it.
    """


printUserName()
getFullname()
fullname = updateFullname()
printFullname(fullname=fullname)
getAge()