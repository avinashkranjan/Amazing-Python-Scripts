# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:40:09 2020

@author: Mansi
"""
import random
import os
import game_config as gc

from pygame import image, transform

animals_count = dict((a, 0) for a in gc.ASSET_FILES)


def available_animals():
    return [animal for animal, count in animals_count.items() if count < 2]


class Animal:
    def __init__(self, index):
        self.index = index
        self.name = random.choice(available_animals())
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        self.skip = False
        self.image = image.load(self.image_path)
        self.image = transform.scale(
            self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))
        self.box = self.image.copy()
        self.box.fill((200, 200, 200))

        animals_count[self.name] += 1
