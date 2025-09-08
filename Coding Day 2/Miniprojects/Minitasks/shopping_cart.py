print("-------------Shopkart-------------")

foods=[]
price=[]
total=0
while True: #this enters all the food we will type to the "foods" list.
 food= input("Which foods would you like to buy?(q to quit): ")

 if food.lower()=="q":
  break

 foods.append(food)

for food in foods:  # assigns prices(that we will enter) to each food we entered in "foods" list.
 mrp =input("Enter the price of each food you bought: ")
 if mrp=="q":
  break
 mrp=float(mrp) #converts the prices we entered in price list from string data type to float
 price.append(f"{mrp:.2f}")
 total += mrp  #adds all the values in in the price list


# print(f"The list of foods you bought are : {foods}")
# print(f"The price of each food you bought are: {price}")   

print(f"the stuff you brought are: \n{foods}")
print(f"these are the prices for each of the stuff bought: \n{price}")

print(f"the total price is :\u20B9{total:.2f}")


