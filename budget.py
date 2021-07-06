class Category:

  def __init__(self, category):
    self.category = category
    self.balance = 0
    self.ledger = []
  
  def __str__(self):
    string = self.category.center(30, '*') + "\n"
    for item in self.ledger:
      amount = item["amount"]
      amount_with_2_decimal = f'{amount:.2f}'
      description = item["description"]
      string += f'{description[:23].ljust(23)}{amount_with_2_decimal.rjust(7)}\n'
    string += f'Total: {self.balance:.2f}'
    return string

  def deposit(self, amount, description=None):
    self.balance += amount
    if description:
      self.ledger.append({"amount": amount, "description": description})
    else:
      self.ledger.append({"amount": amount, "description": ""})

  def withdraw(self, amount, description=None):
    if self.check_funds(amount):
      self.balance -= amount
      if description:
        self.ledger.append({"amount": -amount, "description": description})
      else:
        self.ledger.append({"amount": -amount, "description": ""})
      return True
    else:
      return False
    
  
  def get_balance(self):
    return self.balance

  
  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True

  def transfer(self, amount, destination_category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + destination_category.category)
      destination_category.deposit(amount, "Transfer from " + self.category)
      return True
    else:
      return False




def create_spend_chart(categories):
  all_categoris = []
  spent_each_category = []
  percentage_each_category = []
  # Getting names of all the categories
  for category in categories:
    total_spent = 0
    all_categoris.append(category.category)
    for x in category.ledger:
      if x["amount"] < 0:
        total_spent -= x["amount"]
    spent_each_category.append(total_spent)
  for x in spent_each_category:
    percentage = round(x / sum(spent_each_category), 2) * 100
    percentage_each_category.append(percentage)
  
  bar_chart = "Percentage spent by category\n"
  all_bars = range(100, -10, -10)
  for bar in all_bars:
    bar_chart += str(bar).rjust(3) + "| "
    for x in percentage_each_category:
      if x >= bar:
        bar_chart += "o  "
      else:
        bar_chart += "   "
    bar_chart += "\n"
  bar_chart += '    ----' + '---' * (len(all_categoris) - 1) + '\n     '
  
  # Finding category name with longest length
  longest_name_length = len(all_categoris[0])

  for x in all_categoris:
    if len(x) > longest_name_length:
      longest_name_length = len(x)
  # Printing characters of each category
  for x in range(longest_name_length):
    for y in all_categoris:
      if x < len(y):
        bar_chart += y[x] + '  '
      else:
        bar_chart += '   '
    if x < longest_name_length - 1:
      bar_chart += "\n     "
  return bar_chart
