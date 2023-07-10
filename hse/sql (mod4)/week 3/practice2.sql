SELECT continent, country.name AS country, language AS lngname, LEFT(language, 3), c2.population * percentage AS lngcode
FROM country
JOIN (
    SELECT *
    FROM city
    WHERE city.population / (
        SELECT MAX(city.population)
        FROM city
        JOIN country c ON city.id = c.capital
    ) >= 0.8
) AS c2 ON country.code = c2.countrycode
JOIN countrylanguage c3 ON country.code = c3.countrycode
ORDER BY lngname, lngcode;