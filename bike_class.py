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
import copy


    
class Bicycle(object):

    # Info about the Bike
    def __init__(self, model):
        """ Class construtor """
        self.model_name = model

    def weight(self, B_weight):
        self.weight = B_weight

    def cost_to_produce(self, B_cost_to_produce):
        self.cost_to_produce = B_cost_to_produce

class BikeShops(object):
    
    def __init__(self, B_shop_name, B_diff_bike, B_margin):
        self.Shop_Name = B_shop_name
        self.diff_bike = B_diff_bike
        self.B_margin = B_margin
        self.inventory = []
    
    def add_bike(self, newbike):
        self.inventory.append(BikeShopsbike(newbike, self.B_margin)) 
        
    def sold_bike(self, bike):
        self.inventory.remove(bike)

    def list_inventory(self):
        return copy.copy(self.inventory)


class BikeShopsbike(Bicycle):

    # Info about the bike store

    def __init__(self, other, B_margin):
        self.sell_margin = B_margin

    def __new__(cls, other, B_margin):
        if isinstance(other, Bicycle):
            other = copy.copy(other)
            other.__class__ = BikeShopsbike
            other.sell_margin = B_margin
            return other
        return object.__new__(cls)

    def saleprice(self):
        percent = float(self.sell_margin) / 100
        self.price = self.cost_to_produce * (1 + percent)
        return self.price

    def profit(self):
        return self.price - self.cost_to_produce



class Customers(BikeShops):
    def __init__(self, cust_name, allowance):
        self.cust_name = cust_name
        self.to_spend = allowance

        if self.to_spend >= self.salesprice:
            can_buy = True
        else:
            can_buy = False
        return can_buy

