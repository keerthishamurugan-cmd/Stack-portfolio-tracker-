stockprices = {
         "APPLE": 100,
         "TESLA":  250,
         "GOOGLE":150,
         "AMAZON":180
}
totalInvestment = 0
stockname = input("Enter stock name:").upper()
quantity = int(input('Enter quantity:'))

if stockname in stockprices:
    price = stockprices[ stockname]
    totalInvestment = price*quantity
    
    print("StockName:",stockname)
    print("Price Per Stock:",price)
    print("Quantity:",quantity)
    print("Total Investment:",totalInvestment)
    
    with open("stockresult.txt","w")as file:
        file.write(f"stock:{stockname}\n")
        file.write(f"Quantity:{quantity}\n")
        file.write(f"Total:{totalInvestment}")
    print("\nResult saved in stock_result.txt")
else:
    print("stock not available")
    
   