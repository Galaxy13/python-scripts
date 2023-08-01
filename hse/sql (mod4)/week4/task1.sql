with c_c as

( select countryregioncode, productcategoryid id, name as categoryname

from

(select distinct countryregioncode

from address) as countries

cross join

(select productcategoryid, name
from productcategory) as cat
),
orders as (
select h.salesorderid,
h.duedate, h.billtoaddressid,
d.productid, h.taxamt, pc.productcategoryid id, a.countryregioncode country
from salesorderdetail as d
join salesorderheader as h using(salesorderid)
join product as p using (productid)
join productsubcategory as ps using (productsubcategoryid)
join productcategory as pc using (productcategoryid)
join address as a on a.addressid = h.billtoaddressid
where h.subtotal=0)
select * from c_c
left join orders
on orders.id = c_c.id
and orders.country = c_c.countryregioncode;