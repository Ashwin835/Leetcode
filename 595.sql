/* Write your PL/SQL query statement below */

SELECT World.name, World.population, area
FROM World WHERE area>=3000000 OR World.population>=25000000;
