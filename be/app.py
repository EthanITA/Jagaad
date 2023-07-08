from flask import Flask, request, make_response,jsonify

from models.message import Message

app = Flask(__name__)


@app.post('/message')
def new_message():
    try:
        message = Message.from_json(request.get_json())
        if message is None:
            return make_response('Bad request', 400)
        message.save()
        return make_response('Created', 201)
    except Exception as e:
        return make_response(str(e), 500)


@app.get('/messages')
def get_messages():
    try:
        messages = Message.get_all()
        fields = ['uuid', 'customerId', 'type', 'amount']
        messages = [{field: getattr(message, field) for field in fields} for message in messages]
        return make_response(jsonify(messages), 200)
    except Exception as e:
        return make_response(str(e), 500)


if __name__ == '__main__':
    app.run()
