import json


def sort(event, context):
    query = event['queryStringParameters']['numbers']
    if query is not None:
        numbers = query_string_to_list(query)
    else:
        numbers = [3, 2, 1]
    numbers.sort()
    return create_response(numbers)


# Helper functions
def query_string_to_list(query_string):
    return list(map(int, query_string.split(',')))


def create_response(result):
    return {
        'statusCode': '200',
        'body': json.dumps(result),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
