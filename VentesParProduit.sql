SELECT c2 AS Produit, SUM(c4) as CA
FROM ventes
WHERE c2 <> 'produit'
GROUP BY c2 


