# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:40:09 2020

@author: Mansi
"""
import os

IMAGE_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 8

ASSET_DIR = 'assets'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
assert len(ASSET_FILES) == 8
