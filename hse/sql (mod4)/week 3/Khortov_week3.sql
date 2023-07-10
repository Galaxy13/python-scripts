select country.name from country where population != 0 order by
        "abs"((((surfacearea / population) / (select max(surfacearea / population) from country where population != 0) * 100) + (gnp / (select max(gnp) from country)) * 100) -
              ((select gnp / (select max(gnp) from country) from country where name='Argentina') * 100 +
              (select surfacearea / population / (select max(surfacearea / population) from country where population != 0) from country where name='Argentina') * 100)) asc limit 10 offset 1