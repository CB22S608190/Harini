







def linearsearchproduct(productList, targetproduct):
 indices = []

 for index, product in enumerate              (productList):
    if product == targetproduct:
      indices.append(index)

 return indices


#Example usage:
products=["shoes","boot","loafer","shoes","sandle" ,"shoes"]
target = "shoes"
target2 = "apple"
result = linearsearchproduct(products,target)
print (result)