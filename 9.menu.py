menu={
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80
}
print("Welcome to our resturant!")
print("Here\'s the menu:")
print("Pizza: Rs 100")
print("Pasta: Rs 120")
print("Burger: Rs 60")
print("Salad: Rs 70")
print("Coffee: Rs 80")
order_total=0

item=input("Enter your first item you want to order:")
if item.lower() in menu:
    order_total+=menu[item]
    print(f"Order of {item} has been added")
else:
    print(f"Ordered item {item} is not available yet!")
        
while True:
    another_item=input("Do you want to order anything else? (Y/N) ")
    if another_item.lower()=='y':
        item2=input("Enter the item you want to order:")
        if item2.lower() in menu:
            order_total +=menu[item2]
            print(f"Order of {item} has been added")
        else:
            print(f"Ordered item {item} is not available yet!")
    else:
        break
print(f"Total amount to pay is {order_total}")

