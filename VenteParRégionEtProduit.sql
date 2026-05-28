SELECT c5, c2 AS region, SUM(c4) as Ventes
FROM ventes
WHERE c2 <> 'produit'
GROUP BY c5, c2