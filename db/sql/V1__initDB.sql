create table message
(
    "customerId" integer not null,
    type         text    not null,
    amount       text    not null,
    uuid         text
        constraint uuid
            primary key
);

comment on column message."customerId" is 'The customerId is the customer unique identifier';

comment on column message.type is 'The type of message received';

comment on column message.amount is 'Amount billed to the customer, as a string with 3 decimals precision';

comment on column message.uuid is 'The message unique identifier';

