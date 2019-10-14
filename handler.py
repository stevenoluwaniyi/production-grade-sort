import json


def sort(event):
    numbers = get_numbers_or_default(event)
    numbers.sort()
    return create_response(numbers)


# Helper functions
def get_numbers_or_default(event):
    query_string = event['queryStringParameters']
    if query_string is not None:
        numbers_string = query_string["numbers"]
        if numbers_string is not None:
            numbers = query_string_to_list(query_string)
        else:
            numbers = [3, 2, 1]
    else:
        numbers = [3, 2, 1]
    return numbers


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
