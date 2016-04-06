from __future__ import print_function

import boto3
import json

from random import sample

from uuid import uuid4

print('Loading random fight file')

dynamodb = boto3.resource('dynamodb')
monster_table = dynamodb.Table('monsters')
fights_table = dynamodb.Table('fights')

# the plan is to not do this everytime a fight is requested, but to cache
# the full monster list with the database connection, reasonable as long as we
# don't have too many monsters
#
# How often lambda reloads the module is an interesting question
all_monster_data = monster_table.scan()

all_monsters = all_monster_data['Items']

def create_random_fight(event, context):
    p1, p2 =  sample(all_monsters, 2)
    fight_uuid = uuid4()
    fights_table.put_item(Item={
    'fight_uuid': fight_uuid.hex, 
    'c1': p1['animal_id'],
    'c2': p2['animal_id'],
    })
    
    return {
            'monster_1_base': p1['base_animal'],
            'monster_1_size': p1['size'],
            'monster_1_size_animal': p1['size_animal'],
            'monster_1_id': p1['animal_id'],
            'monster_1_image': p1['image'],
            'monster_2_base': p2['base_animal'],
            'monster_2_size': p2['size'],
            'monster_2_size_animal': p2['size_animal'],
            'monster_2_id': p2['animal_id'],
            'monster_2_image': p2['image'],
            'fight_uuid': fight_uuid.hex,
        }
