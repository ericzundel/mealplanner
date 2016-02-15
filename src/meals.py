

class Meal:
  def __init__(self, name, day_before_prep=False, leftovers=False):
    """An entry in the meal database.

    :param name: a short name for the recipe
    :param day_before_prep: this meal can be prepped the night before
    :param leftovers: this meal will have leftovers for the following day
    """
    self.name = name
    self.day_before_prep = day_before_prep
    self.leftovers = leftovers

  def __eq__(self, other):
    return self.name == other.name

  def __hash__(self):
    return self.name.__hash__()
