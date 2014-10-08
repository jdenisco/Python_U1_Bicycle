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

from bike_class import *

bike1 = Bicycle('Huffy')
bike1.weight(10)
bike1.cost_to_produce(450)

mystore = Bike_Shops('Jims Bike Store', 1)
    
mystore.cost_to_produce(100)



print ('Bike model %s ' % bike1.model_name)
print ('Bike weight %s ' % bike1.weight)
print ('Cost to build this bike %s ' % bike1.cost_to_produce)
print ('Mystore cost to make %s ' % mystore.cost_to_produce)
print ('Mystore saleprice %s ' % mystore.saleprice(20))
