from coffedata import MENU,resources
import time

water_avail=resources["water"]
milk_avail=resources["milk"]
coffee_avail=resources["coffee"]


def ingrediants(fl):
   flavour=dict(MENU[fl])
   cost=flavour["cost"]
#    print(f"COST FOR {fl} is {cost}..pls proceed to pay")
   ingrediant=dict(flavour["ingredients"])
   fl_water=ingrediant["water"]
   fl_milk=0
   if "milk" in ingrediant:
      fl_milk=ingrediant["milk"]
   fl_coffee=ingrediant["coffee"]
   print(f"amount of resources required milk={fl_milk} coffee={fl_coffee} water={fl_water}")
   return fl_water,fl_milk,fl_coffee,cost

def coins(five=0,two=0,one=0,v=0):
    return 5*five+2*two+one*1

def preparing(w,m,c):
    global water_avail,milk_avail,coffee_avail
    if w<=water_avail and m<=milk_avail and c<=coffee_avail:
       water_avail -= w
       milk_avail -= m
       coffee_avail -= c
       return True
    else:
        return False

while True:
    flavour=input('What do u like to have (espresso/latte/cappuccino):')
    print(
        f'"WATER":{water_avail}\n"MILK":{milk_avail}\n"COFFEE":{coffee_avail}\n'
    )
    water,milk,coffee,cst=ingrediants(flavour)
    value=cst
    if preparing(water,milk,coffee):
        print(f"The cost for {flavour} is {value}....pls proceed to pay")
        f=int(input("enter the number of 5 rupee coin:"))
        t=int(input("enter the number of 2 rupee coin:"))
        o=int(input("enter the number of 1 rupee coin:"))
        sum=coins(five=f,two=t,one=o,v=value)
        if sum==value:
            print("\nUR COFFE WILL BE READY IN FEW MINUTES")
            time.sleep(5)
            print("ENJOY UR COFFE ☕")
            ip=input("do u want another cup:(y/n) ").lower()
            if ip!="y":
               break
        else:
            print(f"\ntotal cost is {value} and paid amount is {sum}....amount will be refunded")
            break
    else: 
        print("Resources are not enough")
    

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")


# is_on = True

# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])








