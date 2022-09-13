marked_price = int(input("Enter the Marked price: "))

if (marked_price > 10000):
    net_price = marked_price - ((20 / 100) * marked_price)
    
elif (marked_price > 7000 and marked_price <= 10000):
    net_price = marked_price - ((15 / 100) * marked_price)
    
elif (marked_price <= 7000):
    net_price = marked_price - ((10 / 100) * marked_price)

print("\nThe net price to pay is", net_price)