create materialized view if not exists product1 as
    select pc.productcategoryid pcid,
           p.productid productid,
           pc.name pcname,
           p.name pname
        from productcategory pc join productsubcategory psc on pc.productcategoryid = psc.productcategoryid
            join product p on psc.productsubcategoryid = p.productsubcategoryid;

create materialized view if not exists product2 as
    select distinct a.countryregioncode
from customer c join customeraddress c2 on c.customerid = c2.customerid join address a on c2.addressid = a.addressid
where c2.addresstype = 'Main Office'