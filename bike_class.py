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
    def __init__(self, model, weight, cost_to_produce):

        self.model_name = model
        self.weight = weight
        self.cost_to_produce = cost_to_produce


class Bike_Shops:
    def __init__(self, shop_name, diff_bike, sell_margin):
        self.Shop_Name = shop_name
        self.diff_bike =  diff_bike
        self.sell_margin = sell_margin
        self.profit = Bicycle.cost_to_produce * ( 1 + sell_margin )


class Customers():
    def __init__(self, cust_name, allowance):
        self.cust_name = cust_name
        self.to_spend = allowance
        if self.to_spend >= Bike_Shops.profit:
            can_buy = True
        else:
             can_buy = False

