from datetime import datetime

from app import db, app


class Message(db.Model):
    __tablename__ = 'message'

    uuid = db.Column(db.Text, primary_key=True)
    customerId = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # type: db.Column

    def __init__(self, uuid: str, customerId: int, type: str, amount: str):
        self.uuid = uuid
        self.customerId = customerId
        self.type = type
        self.amount = amount

    @staticmethod
    def from_json(json) -> 'Message' or None:
        """
        The method creates a Message object from json while validating it.
        :param json:
        :return:
        """
        try:
            # Checking for amount's precision
            if len(json['amount'].split('.')[-1]) <= 3:
                raise Exception
            return Message(
                str(json['uuid']),
                int(json['customerId']),
                str(json['type']),
                str(json['amount'])
            )
        except:
            return None

    def save(self) -> None:
        """
        The method add the message to the table.
        Supposing that newly added messages are not duplicated.
        :return:
        """
        with app.app_context():
            db.session.add(self)
            db.session.commit()

    @staticmethod
    def get_all(start: datetime, end: datetime) -> list['Message']:
        """
        The method returns all messages between start and end.
        :return:
        """
        with app.app_context():
            return db.session.query(Message).filter(Message.created_at.between(start, end)).all()

    @staticmethod
    def get_customer_stats(customer_id, messages: list['Message']) -> list[dict]:
        """
        The method returns a list of stats for a customer grouped by message type.
        [
            {
                "type": "A",
                "count": 1,
                "totalAmount": 0.012
            },
        ]

        :param customer_id:
        :param messages:
        :return:
        """
        customer_messages = [message for message in messages if message.customerId == customer_id]

        category_stats = {}
        for message in customer_messages:
            if message.type not in category_stats:
                category_stats[message.type] = {
                    'type': message.type,
                    'count': 0,
                    'totalAmount': 0
                }
            category_stats[message.type]['count'] += 1
            category_stats[message.type]['totalAmount'] += float(message.amount)
        return list(category_stats.values())
