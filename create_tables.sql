CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(255) PRIMARY KEY,
    billing_address VARCHAR(255),
    mailing_address VARCHAR(255),
    created_date TIMESTAMP NOT NULL,
    close_date TIMESTAMP,
    email__c VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone VARCHAR(255),
    carrier VARCHAR(255), 
    planName VARCHAR(255),
    premium  INT,
    product VARCHAR(255),
    effective_date TIMESTAMP,
    expiration_date TIMESTAMP,
    stage VARCHAR(255),
    CONSTRAINT fk_billing_address
        FOREIGN KEY (billing_address)
            REFERENCES addresses (address_id)
            ON DELETE SET NULL,
    CONSTRAINT fk_mailing_address
        FOREIGN KEY (mailing_address)
            REFERENCES addresses (address_id)
            ON DELETE SET NULL,
);

-- carrier, product, and stage would be foreign keys to tables not in this db
-- premium is stored in US cents

CREATE TABLE IF NOT EXISTS addresses (
    address_id VARCHAR(255) PRIMARY KEY,
    street VARCHAR(255),
    city VARCHAR(255),
    zip VARCHAR(255),
    state VARCHAR(255)
);