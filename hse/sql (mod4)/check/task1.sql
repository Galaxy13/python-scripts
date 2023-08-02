select * from
             (select * from city ct where ct.population > 8000000 and not exists
                 (select 1 from country c where c.capital=ct.id)) as t;