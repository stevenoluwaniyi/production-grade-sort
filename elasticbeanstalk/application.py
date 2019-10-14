from flask import Flask, request
import json

application = Flask(__name__)


@application.route('/')
@application.route('/sort')
def sort():
    query = request.args.get('numbers')
    numbers = [3, 2, 1]
    if query is not None:
        numbers = query_string_to_list(query)
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


if __name__ == "__main__":
    application.run()
