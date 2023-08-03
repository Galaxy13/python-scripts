insert into company_sales (cid, salesamt, year, quarter_yr, qr, categoryid, ccls)  (select c2.id, sum(linetotal), extract(year from orderdate), extract(quarter from orderdate),
       cast(extract(year from orderdate) as text) || '.' || cast(extract(quarter from orderdate) as text),
       p2.productcategoryid, abc.cls
from salesorderdetail sd join salesorderheader sh on sd.salesorderid = sh.salesorderid
                                            join customer c on sh.customerid = c.customerid
                                            join company c2 on c2.cname = c.companyname
                                            join product p on sd.productid = p.productid
                                            join productsubcategory p2 on p.productsubcategoryid = p2.productsubcategoryid
                                            join company_abc abc on abc.cid = c2.id and abc.year = extract(year from orderdate)
group by c2.id, extract(year from orderdate), extract(quarter from orderdate), p2.productcategoryid, abc.cls
order by c2.id)