price = int(input("상품의 가격: "))

if price>20000 :
    ship_cost = 0
else :
    ship_cost = 3000

print(f"배송비 = {ship_cost}")