products=[]
#ingreso por teclado de items de la lista
itemslist=int(input("Put the items size of list: "))
for i in range(itemslist):
    value=input("Put the name of your list: ")
    products.append(value)
print(products)
for j in products:
    print(j)
value2=int(input("Select the product to print: "))
selection=products[value2]
print(selection)