#!/usr/bin/python

from json import load

import boto3

with file('initial_fighting_animals.json') as f:
    initial_database = load(f)

dynamodb = boto3.resource('dynamodb')
monster_table = dynamodb.Table('monsters')

animal_to_image_map = initial_database['animal_to_image_map']

for monster_hash in initial_database['monsters']:
    monster_hash.update( {'image': 
                          animal_to_image_map[monster_hash['base_animal']] }
                         )
    monster_hash['animal_id'] = monster_hash['primary_key']
    del monster_hash['primary_key']
    
    monster_table.put_item(Item=monster_hash )

    
