-- Update first 10,000 rows
UPDATE scheme_data SET flag = 1 -- WHERE  -- active= 1  
LIMIT 10000; 

-- Update next 10,000 rows
UPDATE scheme_data SET flag = 2 WHERE -- active= 1  AND 
flag NOT IN (1) 
LIMIT 10000;

-- Update next 10,000 rows
UPDATE scheme_data SET flag = 3 WHERE  -- active= 1  AND 
flag NOT IN (1,2) 
LIMIT 10000;


-- Update next 10,000 rows
UPDATE scheme_data SET flag = 4 WHERE -- active= 1  AND 
flag NOT IN (1,2,3) 
LIMIT 10000;

-- Update next 6,000 rows
UPDATE scheme_data SET flag = 5 WHERE -- active= 1  AND 
flag NOT IN (1,2,3,4) 
LIMIT 10000;

SELECT s.flag,COUNT(*) FROM scheme_data s GROUP BY s.flag;

UPDATE scheme_data SET flag=0,ACTIVE=1 
 