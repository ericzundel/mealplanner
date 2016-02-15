from random import randint
from meals import Meal

class MealChooser:
  def __init__(self, meals):
    self.meals = set(meals)

  def choose(self, num_days):
    """Choose meals for the next few days."""
    if (len(self.meals) < num_days):
      raise Exception(
      "There are only {} meals defined. Can't choose for {} days".format(len(self.meals), num_days))
    remaining = list(self.meals)
    chosen = []
    # Look for a new meal for each day for num_days
    days_left = num_days
    while days_left > 0:
      # Choose a random meal from the meals remaining
      random_index = randint(0, len(remaining) - 1)
      # Remove the meal from the remaining and add it to chosen
      chosen_meal = remaining.pop(random_index)
      chosen.append(chosen_meal)
      days_left = days_left - 1
      if chosen_meal.leftovers == True and days_left > 0:
        chosen.append(Meal("leftover " + chosen_meal.name))
        days_left = days_left - 1
    return chosen
