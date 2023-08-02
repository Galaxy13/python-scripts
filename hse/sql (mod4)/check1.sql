select * from

(select c.name,

abs((c.gnp/(select gnp from country 

order by gnp desc limit 1)*100 + (c.surfacearea/c.population)/(select surfacearea/population as sp from country

where population > 0 

order by sp desc limit 1)*100)-(arg.gnparg+arg.apcarg))as criterion

from

((select * from

(select name,

gnp/(select gnp from country 

order by gnp desc limit 1)*100 as gnparg,

(surfacearea/population)/(select surfacearea/population as sp from country

where population > 0 

order by sp desc limit 1)*100 as apcarg

from country

where population >0) as q

where name = 'Argentina') as arg 

cross join country as c)

where c.population > 0 and c.name !='Argentina'

order by criterion asc limit 10) as res