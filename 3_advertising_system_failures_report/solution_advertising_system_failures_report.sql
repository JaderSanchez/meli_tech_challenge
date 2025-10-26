SELECT 
	CONCAT(CU.first_name, ' ', CU.last_name) AS 'customer',
  COUNT(*) AS 'failures'
FROM customers AS CU
INNER JOIN campaigns AS CA ON CA.customer_id = CU.id
INNER JOIN events AS E ON E.campaign_id = CA.id
WHERE E.status = 'failure'
GROUP BY CU.first_name, CU.last_name
HAVING COUNT(*) > 3;
