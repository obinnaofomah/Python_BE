def list_converter(scrambled_list, target_word):
    """
    Question 1
    Write a function that converts a scattered list to become a word
    For example

    word = humble
    list = ["h","l","m","u","b","e"]

    return
    -----
    String

    """

    new_word = ""
    scrambled_str = "".join(scrambled_list).lower()

    for element in target_word.lower():
        if element in scrambled_str:
            new_word += element
        else:
            return "word not found"

    return new_word


def word_generator(scrambled_list, target_words):
    """
    Question 2

    Write a function that generates as many words from a scrambled list given a list of words

    e.g
    list_of_words = ["apple", "fruits", "mango", "heal"]
    scrambled_list = ["a","p","l","r","u","i","t","s","h","e","n","g","o","f"]

    return
    ---------
    List
    """

    word_list = []

    for i in range(len(scrambled_list)):
        scrambled_list[i] = scrambled_list[i].lower()

    for word in target_words:
        new_word = ""

        for character in word.lower():
            if character not in scrambled_list:
                print(f"{character} not in {word}")
                break
            else:
                new_word += character

        word_list.append(new_word)

    for word in word_list:
        if len(word) == 0:
            word_list.remove(word)

    return word_list


def string_converter(string_word):
    """
    Question 3

    Write a function that converts a string to numbers removing any even digit from that number

    example
    dog = 4157 = 157

    """
    num_rep = ""
    num_value = ""
    alpha_list = list("abcdefghijklmnopqrstuvwxyz")

    for element in string_word:
        index_value = str(alpha_list.index(element) + 1)
        num_rep += index_value

    for value in num_rep:
        if int(value) % 2 == 1:
            num_value += value

    return num_value


print(string_converter("dog"))
