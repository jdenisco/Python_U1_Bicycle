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


class Bicycle(object):

    # Info about the Bike
    def __init__(self, model):
        """ Class construtor """
        self.model_name = model

    def weight(self, B_weight):
        self.weight = B_weight

    def cost_to_produce(self, B_cost_to_produce):
        self.cost_to_produce = B_cost_to_produce


class Bike_Shops(Bicycle):

    # Info about the bike store

    def __init__(self, B_shop_name, B_diff_bike):
        self.Shop_Name = B_shop_name
        self.diff_bike = B_diff_bike

    def saleprice(self, B_margin):
        self.sell_margin = B_margin
        percent = float(self.sell_margin) / 100
        self.price = self.cost_to_produce * (1 + percent)
        print('Price %s ' % self.price)
        return self.price

    def profit(self):
        return self.price - self.cost_to_produce


class Customers(Bike_Shops):
    def __init__(self, cust_name, allowance):
        self.cust_name = cust_name
        self.to_spend = allowance

        if self.to_spend >= self.salesprice:
            can_buy = True
        else:
            can_buy = False
        return can_buy
