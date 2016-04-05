#!/usr/bin/python

import boto3

from random import sample

dynamodb = boto3.resource('dynamodb')
monster_table = dynamodb.Table('monsters')

# the plan is to not do this everytime a fight is requested, but to cache
# along side the database connection
all_monster_data = monster_table.scan()

all_monsters = all_monster_data['Items']

p1, p2 =  sample(all_monsters, 2)

def print_combantant(c):
    print( "%(size)d %(size_animal)s-sized %(base_animal)s" % c)

print_combantant(p1)

print("\n VS. \n")

print_combantant(p2)
