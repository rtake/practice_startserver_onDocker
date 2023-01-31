#! /bin/bash

COMMAND='
CREATE DATABASE test_database;
USE test_database;
CREATE TABLE test_table (name VARCHAR(255), english INT, mathematics INT);
INSERT test_table (name, english, mathematics) VALUES ("Ichiro", 10, 10), ("Jiro", 20, 40), ("Saburo", 30, 90);'

mysql --user=root --password=my-secret-pw --execute="$COMMAND"
