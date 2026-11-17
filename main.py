product = [
    {
        "name": "Ahlgrens bilar",
        "price": 17.5,
        "quantity": 2,
    },
    {
        "name": "Gott och blandat",
        "price": 18.5,
        "quantity": 3,
    },
    {
        "name": "Pringles Sourcream and Onion",
        "price": 35.95,
        "quantity": 2,
    },
    {
        "name": "Marabou Mjölkchoklad",
        "price": 24.9,
        "quantity": 5,
    }
]

totalsumma = 0 

for product in product: 
  print(product["name"])
  print("Pris:", product["price"], "kr")
  print("Antal", product["quantity"], "st")
  
  totalsumma = totalsumma + (product["price"] * product["quantity"])
  print("")
  
  print("Totalsumman:", totalsumma, "kr")