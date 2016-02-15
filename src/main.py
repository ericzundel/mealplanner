#!/usr/bin/env python
from mealchooser import MealChooser
from meals import Meal

MEALS = [
  Meal("pork loin", day_before_prep=True, leftovers=True),
  Meal("fish"),
  Meal("chili", day_before_prep=True, leftovers=True),
  Meal("chicken tenders"),
  Meal("tacos"),
  Meal("ramen"),
  Meal("rice bowl")
]

chooser = MealChooser(MEALS)

chosen_meals = chooser.choose(7)

for order, meal in enumerate(chosen_meals):
  print ("{} : {}".format(order, meal.name))

# t1 = Meal("test1")
# t2 = Meal("test2")
# t3 = Meal("test1")
# print ("Hello t1 == t2 is {}".format(t1 == t2))
# print ("t1 == t3 is {}".format(t1 == t3))
