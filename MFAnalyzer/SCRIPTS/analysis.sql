SELECT 
    d.schemeCode,
    WEEK(s.date) AS week_number,
    MAX(s.nav) AS max_nav,
    MIN(s.nav) AS min_nav,
    ((MAX(s.nav) - MIN(s.nav)) / MIN(s.nav)) * 100 AS rate_of_return,
    s.scheme_name
FROM 
    mfnavdetails s
JOIN 
    scheme_data d ON s.scheme_code = d.schemeCode
WHERE 
    s.date BETWEEN '2024-03-01' AND '2024-03-10'   -- Specify your week start and end dates here
GROUP BY 
    s.scheme_code, WEEK(s.date),s.scheme_name
ORDER BY 
    rate_of_return DESC
LIMIT 
    30; -- Limit the output to top N performing funds, adjust as needed 
select * FROM scheme_data s WHERE s.schemeCode = 151125; 
SELECT * FROM mfnavdetails m where m.scheme_code = 151125
SELECT 
   s.scheme_name,
    WEEK(s.date) AS week_number,
    MAX(s.nav) AS max_nav,
    MIN(s.nav) AS min_nav,
    ((MAX(s.nav) - MIN(s.nav)) / MIN(s.nav)) * 100 AS rate_of_return
FROM 
    mfnavdetails s
JOIN 
    scheme_data d ON s.scheme_code = d.schemeCode
WHERE 
    s.date BETWEEN '2024-02-21' AND '2024-02-30' -- Specify your week start and end dates here
GROUP BY 
    s.scheme_name,s.scheme_code, WEEK(s.date)
ORDER BY 
    rate_of_return DESC
LIMIT 
    10; -- Limit the output to top N performing funds, adjust as needed
SELECT * FROM mfnavdetails m WHERE m.scheme_name LIKE '%Parag Parikh Flexi Cap Fund Direct Growth%' ORDER BY DATE desc 
    
