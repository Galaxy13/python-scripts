select distinct id,
                S,
                case when SRTi <= Sa then 'A'
                when SRTi <= Sb then 'B'
                else 'C' end,
                orderyear from (select c2.id, extract(year from orderdate) as orderyear, sum(subtotal) as S,
       0.8 * SUM(subtotal)  AS Sa,
        0.95 * SUM(subtotal) as  Sb,
        SUM(subtotal) OVER (PARTITION BY extract(year from orderdate) ORDER BY subtotal DESC) AS SRTi
       FROM
            salesorderheader
        JOIN customer c ON c.customerid = salesorderheader.customerid
        JOIN company c2 ON c.companyname = c2.cname
where extract(year from orderdate) in (2012, 2013)
group by c2.id, extract(year from orderdate)) as subquery;

select c2.id, extract(year from orderdate) as orderyear, sum(subtotal) as S,
       sum(subtotal) * 0.8 as Sa,
       sum(subtotal) * 0.95 as Sb,
       sum(sum(subtotal)) over (order by sum(subtotal) desc) as SRTi
       FROM
            salesorderheader
        JOIN customer c ON c.customerid = salesorderheader.customerid
        JOIN company c2 ON c.companyname = c2.cname
where extract(year from orderdate) in (2012, 2013)
group by c2.id, extract(year from orderdate)
order by S desc
