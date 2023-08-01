select
    c.name countryname,
    ct.name cityname,
    ct.population as city_population
 from city as ct
    join country as c on c.code = ct.countrycode
    join (select countrycode, avg(population) as avg_population
          from city
          group by countrycode) as avg
    on ct.countrycode=avg.countrycode
    where ct.population > avg_population
 order by c."name" , ct."name";