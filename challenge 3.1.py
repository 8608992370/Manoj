def linearSearchProduct(productList, targetProduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices


Products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target1 = "shoes"
target2 = "apple"
result = linearSearchProduct(Products, target1)
print(result)