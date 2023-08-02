SELECT ci.*
FROM country co RIGHT JOIN city ci ON co.capital = ci.id
WHERE co.code IS NULL AND ci.population >= 8000000;

SELECT c.name AS countryname, ct.name AS cityname, ct.population AS city_population
FROM city ct JOIN country c ON c.code = ct.countrycode
             JOIN (
                    SELECT countrycode, AVG(population) as avg_population
                    FROM city
                    GROUP BY countrycode
            ) av ON c.code = av.countrycode
WHERE ct.population > av.avg_population
ORDER BY c."name" , ct."name";