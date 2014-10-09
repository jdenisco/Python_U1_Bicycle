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

import json
import bike_class as B

bike1 = B.Bicycle('Huffy')
bike1.weight(10)
bike1.cost_to_produce(450)
bike2 = B.Bicycle('schwinn')
bike2.weight(13)
bike2.cost_to_produce(1450)

mystore = B.Bike_Shops('Jims Bike Store', 1)
mystore.cost_to_produce(450)
print ('Bike model %s ' % bike1.model_name)
print ('Bike weight %s lbs' % bike1.weight)
print ('Cost to build this bike %s ' % bike1.cost_to_produce)
print ('Mystore cost to make %s ' % mystore.cost_to_produce)
print ('Mystore saleprice %s ' % mystore.saleprice(20))
print ('Mystore profit %s ' % mystore.profit())
mystore.add_bike(bike1)
mystore.add_bike(bike2)

for a in mystore.list_inventory():
    print a.model_name

print('------------------')
mystore.sold_bike(bike2)

for c in mystore.list_inventory():
    print c.model_name

# print(json.dumps(mystore.__dict__))
# print(dir(mystore))
