#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: bike-test
#   date: 2014-10-07
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""

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
