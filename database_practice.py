import uuid
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

    [ billing_street,
    billing_state,
    billing_zip,
    billing_city,
    mailing_street,
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
    
    premium_cents = int(premium.replace(".", ""))

    billing_address_id = str(uuid.uuid1())
    mailing_address_id = str(uuid.uuid1())

    billing_insert_query = (
        f"INSERT INTO addresses (address_id, street, city, zip, state) "
        f"VALUES ('{billing_address_id}', '{billing_street}', '{billing_city}', '{billing_zip}', '{billing_state}')"
        )
    mailing_insert_query = (
        f"INSERT INTO addresses (address_id, street, city, zip, state) "
        f"VALUES ('{mailing_address_id}', '{mailing_street}', '{mailing_city}', '{mailing_zip}', '{mailing_state}')"
        )

    user_id = str(uuid.uuid4())

    # print(created_date)
    # print(premium_cents)

    user_insert_query = (
        f"INSERT INTO users (user_id, billing_address_id, mailing_address_id, created_date, "
        f"close_date, email__c, first_name, last_name, "
        f"phone, plan_name, carrier, premium, product, effective_date__c, expiration_date__c, stage) "
        f"VALUES ('{user_id}', '{billing_address_id}', '{mailing_address_id}', '{created_date}', "
        f"'{close_date}', '{email__c}', '{first_name}', '{last_name}', '{phone}', '{plan_name}', "
        f"'{carrier}', '{premium_cents}', '{product}', '{effective_date__c}', '{expiration_date__c}', '{stage}')"
    )

    db_connection.autocommit = True
    cursor = db_connection.cursor()
    cursor.execute(billing_insert_query)
    cursor.execute(mailing_insert_query)
    cursor.execute(user_insert_query)

    # print(first_name)
    return True

def read_all_that_data(db_connection):

    f = open("./interview_test_data_small.csv", "r")

    count = 0
    for line in f:

        quote_fix_line = line.replace("'", "''")
        line_items = quote_fix_line.split(sep=',')
        if line_items[0] == "BillingAddress":
            continue
        put_line_in_db(db_connection, line_items)
    
        count += 1

    f.close

    return count


if __name__ == "__main__":
    connection = create_connection(
        "practice", "servacct", "prop9613velo", "127.0.0.1", "5432"
    )
    count = read_all_that_data(connection)
    print (f"{count} lines read")
