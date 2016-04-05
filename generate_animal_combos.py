#!/usr/bin/python

# this was used to generate initial_fighting_animals.json

from __future__ import print_function

from os import listdir
from random import sample, choice
from json import dumps

FILE_SUFFIX_TO_STRIP = '.jpg'

POPULATIONS = (1, 25, 100)

CREATION_ITERATIONS = 500

COMPONENTS_PER_MONSTER = 2 

# this is a dictionary comprehension
animal_to_image_map = {
    image_file[:-len(FILE_SUFFIX_TO_STRIP)].lower() : image_file
    for image_file in listdir('wikipedia_article_images')    
}

animals = animal_to_image_map.keys()

def assemble_monster_from_parts(animals, size):
    return (size, animals[1], animals[0])

# this is going to be a set comprehension, helps us avoid duplicates
monsters = {
    assemble_monster_from_parts( 
        sample(animals, COMPONENTS_PER_MONSTER),
        choice(POPULATIONS) )
    for i in range(CREATION_ITERATIONS)
}

# these are the two classics, the 1 horse sized duck
# and the 100 duck sized horses
monsters.add( (1, 'horse', 'duck') )
monsters.add( (100, 'duck', 'horse') )

# this is a list comprehension
monsters_array_and_dict = [
    {
        'base_animal': base_animal,
        'size_animal': size_animal,
        'size': size, 
    }
    for (size, size_animal, base_animal) in monsters
]

print( 
    dumps( {
        'animal_to_image_map': animal_to_image_map,
        'monsters': monsters_array_and_dict
    }
    ) # dumps
) # print
