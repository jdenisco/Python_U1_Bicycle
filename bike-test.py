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

import bike_class

bike1 = bike_class.Bicycle
    


bike1.model = 'Huffy' 
bike1.cost_to_produce = 200


print (bike1.model)
print (bike1.cost_to_produce)
