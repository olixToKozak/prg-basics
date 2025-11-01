#Enter price: 24.72
#Enter discount %: 15
#Price with discount: 21.01
#Reduction: 3.71

price = float(input("Enter pirice:"))
discount=int(input("Enter discount %"))

price_with_discouunt=price-price*(discount/100)
reduction=price-price_with_discouunt

print(f"Price: {price:.2f}")
print(f"discount: {discount}")
print(f"price with doiscount: {price_with_discouunt:.2f}")
print(f"reduction: {reduction:.2f}")
