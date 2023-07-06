import numpy as np
import pygame
import sys
import time

problem = [[0, 2, 4, 0, 0, 6, 0, 0, 8], [6, 0, 9, 0, 2, 0, 0, 1, 0],
           [5, 7, 0, 0, 0, 0, 0, 0, 0], [0, 0, 6, 9, 0, 8, 0, 0, 1],
           [0, 8, 1, 0, 0, 0, 6, 5, 0], [7, 0, 0, 3, 0, 1, 8, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 8, 2], [0, 9, 0, 0, 8, 0, 1, 0, 4],
           [8, 0, 0, 2, 0, 0, 5, 9, 0]]

np_problem = np.array(problem)

pygame.init()
screen = pygame.display.set_mode((440, 440))
pygame.display.set_caption('Sudoku Vizualizer')
animation_time = 0.20

image = pygame.image.load('grid.gif')
image_fill = pygame.image.load('fill.gif')
font = pygame.font.SysFont("calibri", 30)

coordinates = []
sta = True

while sta:

    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))

    x, y = 39, 33

    for row in problem:
        temp_co = []
        for col in row:

            if col != 0:
                label = font.render(str(col), 2, (255, 0, 0))
                screen.blit(label, (x, y))

            temp_co.append([x, y])
            x += 43

        x = 39
        y += 43

        coordinates.append(temp_co)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

    fixed_coordinates = [
    ]  # first getting the coordinates where fixed numbers are present
    empty_coordinates = []
    for i, sub_array in enumerate(problem):
        temp = [[i, c] for c, sub_element in enumerate(sub_array)
                if sub_element > 0]
        temp2 = [[i, j] for j, sub_element2 in enumerate(sub_array)
                 if sub_element2 == 0]
        for z in temp:
            fixed_coordinates.append(z)
        for w in temp2:
            empty_coordinates.append(w)

    l, m, r = [0, 3, 6], [1, 4, 7], [2, 5, 8]

    avoid_dict = {idx: [] for idx in list(range(0, len(empty_coordinates)))}

    def generate_bounds(r, c) -> list:

        lower_bound_c = c if c in l else c - 1 if c in m else c - 2
        upper_bound_c = c + 3 if c in l else c + 2 if c in m else c + 1

        lower_bound_r = r if r in l else r - 1 if r in m else r - 2
        upper_bound_r = r + 3 if r in l else r + 2 if r in m else r + 1

        return [lower_bound_c, upper_bound_c, lower_bound_r, upper_bound_r]

    def backtrack(return_coordinates):

        n_r, n_c = empty_coordinates[
            empty_coordinates.index(return_coordinates) -
            1]  # getting back element coordinates

        while [
                n_r, n_c
        ] != empty_coordinates[empty_coordinates.index(return_coordinates) +
                               1]:

            if np_problem[n_r, n_c] != 0:
                avoid_dict[empty_coordinates.index([n_r, n_c
                                                    ])].append(np_problem[n_r,
                                                                          n_c])

            fix_flag = False
            r, c = n_r, n_c
            for num in range(1, 10):

                l_b_c, u_b_c, l_b_r, u_b_r = generate_bounds(r, c)

                if all([
                        num not in np_problem[l_b_r:u_b_r, l_b_c:u_b_c], num
                        not in np_problem[r, :], num not in np_problem[:, c]
                ]):
                    if num not in avoid_dict.get(
                            empty_coordinates.index([n_r, n_c])):
                        np_problem[n_r, n_c], fix_flag = num, True

                        screen.blit(image_fill, coordinates[n_r][n_c])
                        pygame.display.update()

                        label_n1 = font.render(str(num), 2, (0, 0, 200))
                        screen.blit(label_n1, coordinates[n_r][n_c])
                        pygame.display.update()

                        time.sleep(animation_time)

                        break

            if fix_flag:
                n_r, n_c = empty_coordinates[
                    empty_coordinates.index([n_r, n_c]) + 1]

            if not fix_flag:
                np_problem[n_r, n_c] = 0

                screen.blit(image_fill, coordinates[n_r][n_c])
                pygame.display.update()
                time.sleep(animation_time)

                avoid_dict[empty_coordinates.index([n_r, n_c])].clear()
                n_r, n_c = empty_coordinates[
                    empty_coordinates.index([n_r, n_c]) - 1]

    for r in range(9):
        for c in range(9):

            if [r, c] not in fixed_coordinates:

                fix_flag = False

                for num in range(1, 10):

                    l_b_c, u_b_c, l_b_r, u_b_r = generate_bounds(r, c)

                    if all([
                            num not in np_problem[l_b_r:u_b_r, l_b_c:u_b_c],
                            num not in np_problem[r, :], num
                            not in np_problem[:, c]
                    ]):

                        np_problem[r, c], fix_flag = num, True

                        label_n = font.render(str(num), 2, (0, 0, 200))
                        screen.blit(label_n, coordinates[r][c])
                        pygame.display.update()

                        time.sleep(animation_time)

                        break

                if not fix_flag:
                    backtrack([r, c])

    x = input()  # just to hold window from closing
