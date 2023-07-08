from app import db, app


class Message(db.Model):
    __tablename__ = 'message'

    uuid = db.Column(db.Text, primary_key=True)
    customerId = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Text, nullable=False)

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
    def get_all() -> list['Message']:
        """
        The method returns all messages
        :return:
        """
        with app.app_context():
            return db.session.query(Message).all()
