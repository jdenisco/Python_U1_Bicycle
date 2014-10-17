#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: bike-test
#   date: 2014-10-07
#   author: jdenisco
#   email: jimd@jdenisco.com
#
# Copyright © 2014 jdenisco <jimd@jdenisco.com>
#

# TODO: After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.

"""
Description:
"""

# TODO: Import your classes from a separate file.

import bike_class as B
import random

# TODO: Create a bicycle shop that has 6 different bicycle models in stock. The shop should charge its customers 20% over the cost of the bikes.

bike1 = B.Bicycle('Huffy', 1)
bike1.weight(10)
bike1.cost_to_produce(450)
bike2 = B.Bicycle('schwinn', 2)
bike2.weight(9)
bike2.cost_to_produce(550)
bike3 = B.Bicycle('diamondback', 3)
bike3.weight(11)
bike3.cost_to_produce(750)
bike4 = B.Bicycle('trex', 4)
bike4.weight(13)
bike4.cost_to_produce(150)
bike5 = B.Bicycle('royalbaby', 5)
bike5.weight(8)
bike5.cost_to_produce(100)
bike6 = B.Bicycle('dynacraft', 6)
bike6.weight(11)
bike6.cost_to_produce(175)

# TODO: Create a bicycle shop that has 6 different bicycle models in stock. 
# The shop should charge its customers 20% over the cost of the bikes.
mystore = B.BikeShops('Jims Bike Store', 20)
mystore.add_bike(bike1)
mystore.add_bike(bike2)
mystore.add_bike(bike3)
mystore.add_bike(bike4)
mystore.add_bike(bike5)
mystore.add_bike(bike6)

# TODO: Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
jim = B.Customers('Jim', 1000)
lori = B.Customers('Lori', 500)
nicole = B.Customers('Nicole', 200)
inventory = mystore.list_inventory()

# TODO: Print the initial inventory of the bike shop for each bike it carries.
print("")
print('%s initial inventory is:' % mystore.Shop_Name)
print('Model name \tModel number')
for a in inventory:
    print a.model_name.ljust(20), a.model_number
print("")


# TODO: Print the name of each customer, and a list of the bikes offered by the bike shop that they can
# afford given their budget. Make sure you price the bikes in such a way that each customer can 
# afford at least one.
# TODO: Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
customer = [jim, lori, nicole]
customer_couldbuy = dict()
a = []
for cust in customer:
    customer_couldbuy[cust.cust_name] = {}
#    for bike in mystore.list_inventory():
    for bike in inventory:
        if int(cust.allowance) >= int(bike.saleprice()):
            print ('%s can afford to buy %s model number %s' % (cust.cust_name, bike.model_name, bike.model_number))
            a.append(bike.model_number)
    customer_couldbuy[cust.cust_name] = a
    if not customer_couldbuy[cust.cust_name]: 
        print('All bikes you can afford %s have been sold. Sorry, please check back later' % cust.cust_name)
        print("")
    else:
        ran_pick = random.choice(customer_couldbuy[cust.cust_name])
        for i in inventory:
            if i.model_number == ran_pick:
                print("")
                print('%s is going to buy the %s model number %s.' % (cust.cust_name, i.model_name, i.model_number))
                print("")
                inventory.remove(i)
    a = []

print('Model name \tModel number')
for a in inventory:
    print a.model_name.ljust(20), a.model_number

print('------------------')
