select car.cid, car.make, sum(res.days)

from res, car

where res.cid = car.cid

group by car.make, car.cid;