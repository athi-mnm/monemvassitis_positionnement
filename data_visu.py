import plotly.express as px
import pandas as pd

mydata = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
ca = mydata.qte*mydata.prix
mydata.insert(4, "chiffre", ca)
#print(mydata)

vente_prod = px.pie(mydata, values='qte', names='produit', title='quantité vendue par produit')
vente_prod.write_html('ventes-par-produits.html')
print('ventes-par-produit.html généré avec succès !')

ca = mydata.qte * mydata.prix
ca_prod = px.bar(mydata, x="region", y="chiffre", color="produit", barmode="group")
ca_prod.write_html('ca-par-produits.html')
print('ca-par-produit.html généré avec succès !')