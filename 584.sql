
/* Write your PL/SQL query statement below */

SELECT Customer.name FROM Customer

WHERE

referee_id!=2 OR referee_id IS NULL;


/*
For NULL values in a table, using IS will return true/false for unknown, while == will set it equal to unknown
*/
