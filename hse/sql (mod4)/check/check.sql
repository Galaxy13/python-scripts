select  c.name countryname,  ct.name cityname,  ct.population
 as city_population
 from city as ct
    join country as c on c.code = ct.countrycode
    join (select avg(population)  as avg_population, countrycode
        from city
        group by countrycode) as avg_t on avg_t.countrycode =c.code
    where  ct.population > avg_population
 order by c."name" , ct."name";