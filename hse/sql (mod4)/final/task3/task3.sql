insert into company (cname, countrycode, city)
select distinct c.companyname, a.countryregioncode, a.city from customer c join customeraddress c2 on c.customerid = c2.customerid
                        join address a on a.addressid = c2.addressid
where c2.addresstype = 'Main Office'