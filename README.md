## What is this?
This project is a technical test for a Senior Python Developer position at Jagaad.

The project structure is divided into two parts:
- `be`: the backend, a Python 3.11 application using **Flask** and **SQLAlchemy**
- `db`: the database migration scripts, using **Flyway** and **PostgreSQL**


Refer to the [requirements' .pdf](Jagaad%20_%20Senior%20Python%20Engineer%20-%20Test.pdf) for more information.

## How to run it?
### Requirements
- Docker
- (Optional) Python 3.11 for running the tests

### Steps
1. Clone this repository
2. In the project root, run `docker-compose up --build -d` to build the containers and run them in the background
3. (Optional) Run test `cd ./be && python -m unittest discover`

### Endpoints
- `POST /message`: create a new message
- `GET /messages/stats`: get the stats of messages from start to end date

### Example in the browser console
#### Create a message
```javascript
fetch('http://0.0.0.0:3000/message', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        customerId: 1,
        type: 'A',
        amount: '0.022',
        uuid: 'a596b362-08be-419f-8070-9c3055566ee'
    })
})
```

#### Get the stats
```javascript
fetch('http://0.0.0.0:3000/messages/stats?start_date=2023-01-01&end_date=2023-12-31').then(res => res.json()).then(console.log)

// [{"customerId":1,"messages":[{"count":1,"totalAmount":0.022,"type":"A"}]}]

```
