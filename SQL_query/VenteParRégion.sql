SELECT c5 AS Region, SUM(c4) as Ventes
FROM ventes
WHERE c5 <> 'region'
GROUP BY c5
