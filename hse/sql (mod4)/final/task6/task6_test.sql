insert into plan_data (versionid, country, quarterid, pcid, salesamt) select 'N' as versionid, countrycode, quarterid, categoryid as pcid, salesamt from (WITH subquery1 AS (select cid, salesamt as sales1, quarter_yr, categoryid from company_sales
where year=2012 and ccls in ('A', 'B')),
subquery2 AS (select cid, salesamt as sales2, quarter_yr, categoryid from company_sales
where year=2013 and ccls in ('A', 'B'))
SELECT
    COALESCE(sq1.cid, sq2.cid) AS cid,
    COALESCE(sq1.quarter_yr, sq2.quarter_yr) AS quarterid,
    COALESCE(sq1.categoryid, sq2.categoryid) AS categoryid,
    case when sq1.sales1 = 0 and sq2.sales2 = 0 then 0
        else (COALESCE(sq1.sales1, 0) + COALESCE(sq2.sales2, 0)) / 2 end as salesamt
FROM subquery1 sq1
FULL outer JOIN subquery2 sq2
    ON sq1.cid = sq2.cid
    AND sq1.quarter_yr = sq2.quarter_yr
    AND sq1.categoryid = sq2.categoryid) as sq3
join company c on c.id=sq3.cid;

select * from country_managers
where username='kirill'