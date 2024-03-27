priceMerchandise = float(input('Enter the price of merchandise: R$'))
discountPorcentage = float(input('Porcentage discount: %'))

discount = priceMerchandise * (discountPorcentage/100)
newPrice = priceMerchandise - discount
print(f'The discount amount R${discount}\nPrice to pay: R${newPrice}')
