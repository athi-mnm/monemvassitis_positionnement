SELECT c2 AS produit, SUM(c4) as Ventes, SUM(c3*c4) as CA
FROM ventes
WHERE c2 <> 'produit'
GROUP BY c2 