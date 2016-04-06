from __future__ import print_function

import boto3
import json

from random import sample

from uuid import uuid4

print('Loading fight result file')

dynamodb = boto3.resource('dynamodb')
fights_table = dynamodb.Table('fights')


def fight_result(event, context):
    fight = fights_table.get_item(Key={'fight_uuid': event["uuid"] })["Item"]
    winner_int = int(event["winner"])
    if 'winner' not in fight and winner_int in (fight["c1"], fight["c2"]):
        fight['winner'] = winner_int
        fights_table.put_item(Item=fight)
    return {}