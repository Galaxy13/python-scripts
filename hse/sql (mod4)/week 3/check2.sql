select * from (

(select 'GLE' indicator,

(select

lifeexpectancy as FerederalRepublic

from country

where lifeexpectancy is not null and governmentform = 'Federal Republic'

order by lifeexpectancy desc limit 1),

(select

lifeexpectancy as Republic

from country

where lifeexpectancy is not null and governmentform = 'Republic'

order by lifeexpectancy desc limit 1),

(select

lifeexpectancy as others

from country

where lifeexpectancy is not null and governmentform not in ('Federal Republic', 'Republic')

order by lifeexpectancy desc limit 1)

from country

limit 1)

union

(select 'LLE' indicator,

(select

lifeexpectancy as FerederalRepublic

from country

where lifeexpectancy is not null and governmentform = 'Federal Republic'

order by lifeexpectancy asc limit 1),

(select

lifeexpectancy as Republic

from country

where lifeexpectancy is not null and governmentform = 'Republic'

order by lifeexpectancy asc limit 1),

(select

lifeexpectancy as others

from country

where lifeexpectancy is not null and governmentform not in ('Federal Republic', 'Republic')

order by lifeexpectancy asc limit 1)

from country

limit 1)

) as res