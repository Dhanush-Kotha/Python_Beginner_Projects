menu={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":110,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":120,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":175,
    }

}
profit=0
resources={
    "water":500,
    "milk":200,
    "coffee":100,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def process_coins():
    print("Please insert coins.")
    total=0
    coins_five=int(input("how many 5Rs coins?: "))
    coins_ten=int(input("how many 10Rs coins?: "))
    coins_twenty=int(input("how many 20Rs coins?: "))
    coins_fifty=int(input("how many 50Rs coins?: "))
    total=5*coins_five + 10*coins_ten + 20*coins_twenty + 50*coins_fifty
    return total
def is_transaction_successful(money_received, drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is Rs{change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
            resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
is_on=True
while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs{profit}")
    else:
        drink=menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            global coins_five, coins_ten, coins_twenty, coins_fifty
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
else:
    print("Invalid choice.")