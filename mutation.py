import os
import json
from botocore.vendored import requests

ACCESS_KEY = os.environ['ACCESS_KEY']
HGE_URL = 'http://34.237.245.212/v1alpha1/graphql'
HEADERS = {
    'Content-Type': 'application/json',
    'X-Hasura-Access-Key': ACCESS_KEY,
}

query = """
mutation updateNoteRevision ($noteId: Int!, $data: String!) {
  insert_note_revision (objects: [
    {
      note_id: $noteId,
      note: $data
    }
  ]) {
    affected_rows
  }
}
"""

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
    except:
        return {
            "statusCode": 400,
            "body": json.dumps({'message': 'Unable to parse request body'})
        }
    data = body['data']
    qv = {'noteId': data['id'], 'data': '{} processed with python'.format(data['note'])}
    jsonBody = {'query': query, 'variables': qv}

    resp = requests.post(HGE_URL, data=json.dumps(jsonBody), headers=HEADERS)
    my_json = resp.json()
    print(my_json)
    return {
        "statusCode": 200,
        "body": json.dumps({'message': 'success'})
    }
