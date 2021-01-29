import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def put_line_in_db(db_connection, line_items):
    
    [ billing_address,
    billing_state,
    billing_zip,
    billing_city,
    mailing_address,
    mailing_state,
    mailing_zip, 
    mailing_city,
    created_date,
    close_date,
    email__c,
    first_name,
    last_name,
    phone,
    plan_name,
    carrier, 
    premium,
    product,
    effective_date__c,
    expiration_date__c,
    stage ] = line_items
    
    print(stage)
    return None

def read_all_that_data(db_connection):

    f = open("./interview_test_data_small.csv", "r")

    for line in f:

        line_items = line.split(sep=',')
        put_line_in_db(db_connection, line_items)
    
    f.close

if __name__ == "__main__":
    connection = create_connection(
        "practice", "servacct", "prop9613velo", "127.0.0.1", "5432"
    )
    read_all_that_data(connection)
