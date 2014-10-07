#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: bike_store
#   date: 2014-10-07
#   author: jdenisco
#   email: jimd@jdenisco.com
#
# Copyright © 2014 jdenisco <jimd@jdenisco.com>
#

"""
Description:
"""


class Bicycle:
    model_name = model
    weight = weight
    cost_to_produce = cost_to_produce


class Bike_Shops:
    Shop_Name = shop
    diff_bike =  bike
    sell_margin = margin
    profit = Bicycle.cost_to_produce * ( 1 + sell_margin )


class Customers():
    cust_name = name
    to_spend = allowance
    if to_spend >= Bike_Shops.profit:
        can_buy == True
    else:
        can_buy == False

