select 'GLE' as Indicator, max(case when governmentform='Republic' then lifeexpectancy else null end) as Republic,
        max(case when governmentform='Federal Republic' then lifeexpectancy else null end) as Federal_Republic,
        max(case when governmentform not in ('Republic', 'Federal Republic') then lifeexpectancy else null end) as Other from country
                                                                                                                         as GLE
union select 'LLE' as Indicator, min(case when governmentform='Republic' then lifeexpectancy else null end) as Republic,
        min(case when governmentform='Federal Republic' then lifeexpectancy else null end) as Federal_Republic,
        min(case when governmentform not in ('Republic', 'Federal Republic') then lifeexpectancy else null end) as Other from country
as LLE