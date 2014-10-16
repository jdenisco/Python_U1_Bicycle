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

# TODO: Create a bicycle shop that has 6 different bicycle models in stock. The shop should charge its customers 20% over the cost of the bikes.
# TODO: Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
# TODO: Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. Make sure you price the bikes in such a way that each customer can afford at least one.
# TODO: Print the initial inventory of the bike shop for each bike it carries.
# TODO: Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
# TODO: After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.

"""
Description:
"""

# TODO: Import your classes from a separate file.

import bike_class as B

bike1 = B.Bicycle('Huffy')
bike1.weight(10)
bike1.cost_to_produce(450)
bike2 = B.Bicycle('schwinn')
bike2.weight(13)
bike2.cost_to_produce(1450)

mystore = B.BikeShops('Jims Bike Store', 1, 20)
# mystore.cost_to_produce(450)
print ('Bike model %s ' % bike1.model_name)
print ('Bike weight %s lbs' % bike1.weight)
print ('Cost to build this bike %s ' % bike1.cost_to_produce)
# print ('Mystore cost to make %s ' % mystore.cost_to_produce)
# print ('Mystore saleprice %s ' % mystore.saleprice(20))
# print ('Mystore profit %s ' % mystore.profit())
print('------------------')
print('adding bikes to inventory')
mystore.add_bike(bike1)
mystore.add_bike(bike2)

print('Print inventory')
inventory = mystore.list_inventory()
for a in inventory:
    print('inside inventory %s ' % a.saleprice())
    print('jimd %s ' % a.profit())
    mystore.sold_bike(a)

print('------------------')
print('Sold a bike')
# mystore.sold_bike(bike2)

print('------------------')

print('Print new inventory')
for c in mystore.list_inventory():
    print c.model_name

print('------------------')
# import json
# print(json.dumps(mystore.__dict__))
# print(dir(mystore))
