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
    alpha_dict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }
    num_str = ""
    num_rep = ""

    for element in string_word:
        str_value = str(alpha_dict.get(element))
        num_str += str_value

    for element in num_str:
        if int(element) % 2 == 0:
            pass
        else:
            num_rep += element

    return num_rep


print(
    word_generator(
        ["a", "p", "l", "r", "u", "i", "t", "s", "h", "e", "n", "g", "o", "f"]
    )
)
