from __future__ import print_function
from operator import itemgetter, attrgetter  
import sys, os, time, copy
from point import Point
from space import Space

def read_crossword_config(path):
    crossword = []
    available_word = []
    # open input file
    with open(path) as fin:
        # reading the size of the square crossword
        crossword_size = int(fin.readline()) 
        for row in range(crossword_size):
            # reading the configuration/shape of the crossword
            crossword.append(fin.readline()[:-1])
        # reading the available word to fill the crossword
        available_word = fin.readline().split(';')
        available_word.sort(key=lambda item:(-len(item),item))
    fin.close()
    spaces = generate_all_available_spaces(crossword,crossword_size)
    return crossword_size,crossword,available_word,spaces

def print_crossword(crossword):
    # clear screen in windows OS
    os.system('cls')
    print()
    for each_row in crossword:
        print(each_row)
    print()

def calculate_horizontal_space(crossword,crossword_size):
    horizontal_space_list = []
    for i in range(crossword_size):
        space_length = 0
        starting_point = Point(0,0)
        for j in range(crossword_size):
            if crossword[i][j] == '-':
                if space_length == 0:
                    starting_point = Point(i,j)
                space_length += 1
            elif crossword[i][j] =='#':
                if space_length > 1:
                    horizontal_space = Space('horizontal', space_length, starting_point)
                    horizontal_space_list.append(horizontal_space)
                space_length = 0
        if space_length > 1:
            horizontal_space = Space('horizontal', space_length, starting_point)
            horizontal_space_list.append(horizontal_space)
    return horizontal_space_list

def calculate_vertical_space(crossword,crossword_size):
    vertical_space_list = []
    for j in range(crossword_size):
        space_length = 0
        starting_point = Point(0,0)
        for i in range(crossword_size):
            if crossword[i][j] == '-':
                if space_length == 0:
                    starting_point = Point(i,j)
                space_length += 1
            elif crossword[i][j] =='#':
                if space_length > 1:
                    # Create Object Space containing information of fillable spaces in the crossword
                    vertical_space = Space('vertical', space_length, starting_point)
                    vertical_space_list.append(vertical_space)
                space_length = 0
        if space_length > 1:
            vertical_space = Space('vertical', space_length, starting_point)
            vertical_space_list.append(vertical_space)
    return vertical_space_list        

def generate_all_available_spaces(crossword,crossword_size):
    available_spaces = calculate_horizontal_space(crossword,crossword_size) + calculate_vertical_space(crossword,crossword_size)
    #Sort All Object of Variable Spaces by length property
    available_spaces.sort(key=lambda x:x.length,reverse=True)
    return available_spaces

def fill_horizontal_spaces(crossword,space,word):
    # Fill the - (empty spaces) with word in horizontal position
    temp_crossword = copy.deepcopy(crossword)
    temp_crossword[space.starting_point.x] = crossword[space.starting_point.x][:space.starting_point.y]+ word + crossword[space.starting_point.x][space.starting_point.y+len(word):]
    return temp_crossword

def fill_vertical_spaces(crossword,space,word):
    # Fill the - (empty spaces) with word in vertical position
    temp_crossword = copy.deepcopy(crossword)
    for k in range(len(word)):
        temp_crossword[space.starting_point.x+k] = crossword[space.starting_point.x+k][:space.starting_point.y]+ word[k] + crossword[space.starting_point.x+k][space.starting_point.y+1:]
    return temp_crossword

def validate_filling_spaces(crossword,space,word):
    if(len(word) == space.length):
        count = 0
        for k in range(len(word)):
            if(space.direction=='horizontal'):
                if not crossword[space.starting_point.x][space.starting_point.y+k] in [word[k],'-']:
                    return None
            elif(space.direction=='vertical'):
                if not crossword[space.starting_point.x+k][space.starting_point.y] in [word[k],'-']:
                    return None
            count +=1
        if len(word)-1 == count:
            return None
        else:
            return space.direction
    else:
        return None

def is_full(crossword,crossword_size):
    # Check if the crossword is full with words
    for i in range(crossword_size):
        for j in range(crossword_size):
            if crossword[i][j]=='-':
                return False
    return True

def solve_crossword(crossword,crossword_size,available_space,available_word):
    # Crossword solver
    if available_word==[]:
        if is_full(crossword,crossword_size):
            # Print solved crossword if bruteforcing process are done
            print_crossword(crossword)
            return True
        else:
            return False
    else:
        word = available_word[0]
        for space in available_space:
            direction = validate_filling_spaces(crossword,space,word)
            if(direction == 'vertical'):
                temp_crossword = fill_vertical_spaces(crossword,space,word)
                # recursive call
                if(solve_crossword(temp_crossword,crossword_size,available_space,available_word[1:])):
                    return True
            if direction == 'horizontal':
                temp_crossword = fill_horizontal_spaces(crossword,space,word)
                if(solve_crossword(temp_crossword,crossword_size,available_space,available_word[1:])):
                    return True
        return False

if __name__ == '__main__':
    path = raw_input('>> Insert filename: ')
    crossword_size, main_board, answer_list, spaces = read_crossword_config(path)
    start_time = time.time()
    print(solve_crossword(main_board,crossword_size,spaces,answer_list))
    print("Program execution takes %s seconds" % (time.time() - start_time))