SELECT
MAX(CASE WHEN governmentform = 'Republic' THEN lifeexpectancy ELSE NULL END) AS republic,
MAX(CASE WHEN governmentform = 'Federal Republic' THEN lifeexpectancy ELSE NULL END) AS federal_republic,
MAX(CASE WHEN governmentform NOT IN ('Republic', 'Federal Republic') THEN lifeexpectancy ELSE NULL END) AS other
FROM
country
UNION
SELECT
MIN(CASE WHEN governmentform = 'Republic' THEN lifeexpectancy ELSE NULL END) AS republic,
MIN(CASE WHEN governmentform = 'Federal Republic' THEN lifeexpectancy ELSE NULL END) AS federal_republic,
MIN(CASE WHEN governmentform NOT IN ('Republic', 'Federal Republic') THEN lifeexpectancy ELSE NULL END) AS other
FROM
country