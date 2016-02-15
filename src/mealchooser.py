from random import randint

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
    for item in xrange(0, num_days):
      # Choose a random meal from the meals remaining
      random_index = randint(0, len(remaining) - 1)
      # Remove the meal from the remaining and add it to chosen
      chosen.append(remaining.pop(random_index))
    return chosen
