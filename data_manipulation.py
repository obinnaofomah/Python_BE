def printGroceryLists(list):
    """
    This function collects the grocery lists as a parameter and prints out the different items in the lists to the user.

    grocery_list = ["fruits", "vegetables", "Eggs", "Beacon and Cheese", "Beef", "Lettuce"]
    """
    for grocery in list:
        print(grocery)


def updateList(list, item):
    """
    This function adds an item to the existing grocery lists and returns the updated list

    returns
    -----------
    lists
    """
    list.append(item)
    return list


def deleteList(list, item_to_delete):
    """
    Notice how we add a guard to this function to make sure the item provided is in the list. Sometimes other developers can pass a list that doesn't have that item, and you want to be sure you're checking for that scenario as well.

    returns
    ----------
    list []
    """
    if item_to_delete in list:
        list.remove(item_to_delete)
        return list
    else:
        print(f"{item_to_delete} not found in the list")


# home work 1
def mergeStrings(list, word):
    """
    Using the list given and the word as function parameters, write a function that creates same word from the list. by mergin the contents of the string together

    example:
    list = ["c","a","t","d","b","e"]
    word = "cat"

    return
    -----------
    cat
    """
    new_str = ""
    for element in word:
        if element in list:
            new_str += element
        else:
            return f"{element} not found"
    return new_str


print(mergeStrings(["c", "a", "t", "d", "b", "e"], "tam"))
