#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total

  def add_item(self, title, price, quantity = 1):
    previous_total = self.total
    self.total += price * quantity

  def apply_discount(self):
    self.discount
