insert into company_abc (cid, salestotal, cls, year) with STI_CTE as (
select id, STi, year, sum(STi) over (order by STi desc) as SRTi from (select c2.id, extract(year from orderdate) as year, sum(subtotal) as STi from salesorderheader
    JOIN customer c ON c.customerid = salesorderheader.customerid
    JOIN company c2 ON c.companyname = c2.cname
    WHERE EXTRACT(year FROM orderdate) IN (2012, 2013)
group by c2.id, extract(year from orderdate)) as subquery
group by STi, id, year)
select id, STi, case when SRTi <= 0.8 * (select sum(STI) from STI_CTE) then 'A'
                    when SRTI <= 0.95 * (select sum(STI) from STI_CTE) then 'B'
                    else 'C' end as class, year from STI_CTE