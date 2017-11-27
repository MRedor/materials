DROP TABLE IF EXISTS KeyValue;
CREATE TABLE KeyValue
    (owner TEXT, key TEXT, value TEXT);

INSERT INTO KeyValue
VALUES
    ("user1", "key1", "value1"),
    ("user1", "key2", "value2"),
    ("user2", "key3", "value3"),
    ("admin", "key1", "secret_value");
