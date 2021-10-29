#Version 0.1

#begening of the app with essential info
print("Welcome in this list")
print( )
print("Your information : ")

MoneyYouHave = 25
placeInYourBag = 10

#All element for interact whith
print(f"You have {MoneyYouHave} euros in your pocket and {placeInYourBag} place in your bag")
print( )

HowIsArrengAList = ["name", "number you need", "cost of the product", "place of product in your bag", "have you ever the product"]

Product1 = ["apple", 5, 2, 1, False]
Product2 = ["orange", 2, 3, 2, False]
Product3 = ["Donnut", 1, 12, 4, True]

#Your list with what you need to buy
print("Your list :")

CheckProduct = [Product1[4] == False, Product2[4] == False, Product3[4] == False]

if  CheckProduct[0]:
    print(f"You must buy {Product1[1]} {Product1[0]}")

if CheckProduct[1]:
    print(f"You must buy {Product2[1]} {Product2[0]}")

if CheckProduct[2]:
    print(f"You must buy {Product3[1]} {Product3[0]}")


#The cost of all your product
print( )
print("It Will cost :")

if CheckProduct[0]:
    TotalProduct_1Cost = Product1[1] * Product1[2]
else :
    TotalProduct_1Cost = 0


if CheckProduct[1]:
    TotalProduct_2Cost = Product2[1] * Product2[2]
else :
    TotalProduct_2Cost = 0


if CheckProduct[2]:
    TotalProduct_3Cost = Product3[1] * Product3[2]
else :
    TotalProduct_3Cost = 0


TotalCost = TotalProduct_1Cost + TotalProduct_2Cost + TotalProduct_3Cost

print(f"The total price will be {TotalCost} euros")

if CheckProduct[0]:
    print(f"{Product1[0]} will cost {TotalProduct_1Cost} euros")
else :
    print(f"You already have a {Product1[0]}")

if CheckProduct[1]:
    print(f"{Product2[0]} will cost {TotalProduct_2Cost} euros")
else :
    print(f"You already have a {Product2[0]}")

if CheckProduct[2]:
    print(f"{Product3[0]} will cost {TotalProduct_3Cost} euros")
else :
    print(f"You already have a {Product3[0]}")


HaveEnoughMoney = TotalCost <= MoneyYouHave
MoneyWillRest = MoneyYouHave - TotalCost
MoneyYouMustHave = TotalCost - MoneyYouHave

print("Have you enough money ?")

if HaveEnoughMoney:
    print(f"You have enough money for buy all your list, after buying the entire list, you will have {MoneyWillRest} euros")
else :
    print(f"You don't have enough money, you will have {MoneyYouMustHave} more euros")


#Place your product in your bag
print( )
print("Place in your Bag")

PlaceProduct = [Product1[3] * Product1[1], Product2[3] * Product2[1], Product3[3] * Product3[1]]

TotalPlace = PlaceProduct[0] + PlaceProduct[1] + PlaceProduct[2]

print(f"All your article will take {TotalPlace} place in your bag")

if TotalPlace <= placeInYourBag:
    remainPlace = placeInYourBag - TotalPlace
    print(f"You will have enough place. It will remain {remainPlace} more place")
else:
    morePlace = TotalPlace - placeInYourBag
    print(f"There are not enough place in your bag, you need {morePlace} more place")