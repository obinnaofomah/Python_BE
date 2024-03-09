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


def word_generator(scrambled_list):
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
    scrambled_str = "".join(scrambled_list).lower()

    while True:
        new_word = ""
        target_word = input(
            "Enter the new word to be formed OR PRESS 2 TO TERMINATE:  "
        )
        if target_word == "2":
            break
        else:
            for character in target_word:
                if character in scrambled_str:
                    new_word += character
                else:
                    print(f"{character} not in {scrambled_list}")
                    break
            word_list.append(target_word)

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
        for idx, character in enumerate(alpha_list, start=1):
            if character == element:
                num_rep += str(idx)
                break

    for value in num_rep:
        if int(value) % 2 == 1:
            num_value += value

    return num_value


print(string_converter("dog"))
