# author: Ashir Mehmood
# for Awesome-Python-Scripts repo
import random


string_input = input(" Enter names or random strings ! separated by space")
name_list = string_input.split()


# the random name picker method
def random_name_picker(char_list):
    """This method returns a unique name, from entered list of names"""
    random.shuffle(char_list)
    shuffled_list = char_list
    length = len(shuffled_list)
    random_index = random.randint(1, length)
    new_name = ""
    for x in range(random_index):
        new_name = new_name + (shuffled_list[x])
    print(new_name)
    return new_name


random_name_picker(name_list)    
