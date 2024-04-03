# This is the software part of a coffe machine made by Aditya Upadhyay

import menu
from menu import MENU
from menu import resources
profit=0
def is_resources_sufficient(order_ingredient):
        
    for items in order_ingredient:
        if order_ingredient[items]>=resources[items]:
            print(f"Sorry we don't have enough resources {items}")
            return False
    return True
def update_resource(order_ingredients):
    for items in order_ingredients:
        resources[items]-=order_ingredients[items]
        
        
def process_coin(choice):
    profit=0
    print("Please insert coins for e.g:Only Coin of 5,10,20 is accepted")
    five=int(input("No of coins of 5 :"))
    ten=int(input("No of coins of 10 :"))
    twenty=int(input("No of coins of 20 :"))
    sum=(five*5)+(ten*10)+(twenty*20)
    print(f"You have inserted total {sum} rupees")  
    if sum >=choice:
        change=sum-choice
        print(f"Here is your change {change}") 
        profit+=sum
        return True
    else:
        print(f"Sorry Please insert a total of Rs {choice-sum} more.Collect your money")
        return False
               
is_on=True
while(is_on):
    
    customer_choice=input("What do you like? (espresso/latte/cappuccino) : ")
    
    if customer_choice=="off":
        admin_password=input("Enter the admin password:")
        if admin_password== "aditya" or admin_password=="kajal":
            print("The coffee machine has been turned off")
            is_on=False
        else :
            print("Sorry you don't have the access\n")
            customer_choice=input("What do you like? (espresso/latte/cappuccino) : ")  
            
    elif customer_choice=="report":
        from menu import resources
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}ml")
    else :
        
        drink=MENU[customer_choice]
        print(f"Please insert a total of Rs {drink['cost']}")
        if is_resources_sufficient(drink['ingredients']):
           if process_coin(drink['cost']):
               update_resource(drink['ingredients'])
               print("Here is your coffee ☕☕☕☕")
           
           
           
        