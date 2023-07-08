from datetime import datetime

from flask import Flask, request, make_response, jsonify

from models.message import Message

app = Flask(__name__)


@app.post('/message')
def new_message():
    """
    Create a new message

    properties: {
        uuid: string,
        type: string,
        customerId: int,
        amount: str, # 3 decimals precision
    }

    required: [uuid, type, customerId, amount]

    example: {
        "customerId": 1,
        "type": "A",
        "amount": "0.012",
        "uuid": "a596b362-08be-419f-8070-9c3055566e7c"
    }
    """
    try:
        message = Message.from_json(request.get_json())
        if message is None:
            return make_response('Bad request', 400)
        message.save()
        return make_response('Created', 201)
    except Exception as e:
        return make_response(str(e), 500)


@app.get('/messages/stats')
def get_messages_stats():
    """
    Get messages stats: For every customerId and for every type of message, you want to know how many
    messages have been processed and what is the total amount of that specific type for a date
    interval.

    query: {
        start_date: str, # format: YYYY-MM-DD
        end_date: str, # format: YYYY-MM-DD
    }

    required: [start_date, end_date]

    example: {
        "start_date": "2021-01-01",
        "end_date": "2021-01-31"
    }
    :return:
    [
        {
            "customerId": 1,
            "messages": [
                {
                    "type": "A",
                    "count": 1,
                    "totalAmount": 0.012
                },
            ]
        },
    ]
    """
    try:
        def date_converter(date):
            return datetime.strptime(date, '%Y-%m-%d')

        start_date = date_converter(request.args.get('start_date'))
        end_date = date_converter(request.args.get('end_date'))

        messages = Message.get_all(start_date, end_date)

        customers_id = set([message.customerId for message in messages])
        result = [{
            'customerId': customer_id,
            'messages': Message.get_customer_stats(customer_id, messages)
        } for customer_id in customers_id]

        return make_response(jsonify(result), 200)
    except ValueError:
        return make_response('Bad request', 400)
    except Exception as e:
        return make_response(str(e), 500)


if __name__ == '__main__':
    app.run()
