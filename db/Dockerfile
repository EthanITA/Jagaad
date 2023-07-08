FROM redgate/flyway:9.19.4

USER root

COPY sql /flyway/sql

# Copy the Flyway configuration file (as a template)
COPY flyway.conf /flyway/conf/flyway.conf

CMD ["migrate"]
