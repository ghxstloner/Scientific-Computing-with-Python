class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=None):
        if description is None:
            description = ''
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=None):
        if amount > self.balance:
            return False
        if description is None:
            description = ''
        self.ledger.append({"amount": -amount, "description": description})
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination_category):
        if amount > self.balance:
            return False
        self.ledger.append({
            "amount": -amount,
            "description": "Transfer to {}".format(destination_category.name)
        })
        destination_category.ledger.append({
            "amount": amount,
            "description": "Transfer from {}".format(self.name)
        })
        self.balance -= amount
        destination_category.balance += amount
        return True

    def check_funds(self, amount):
        return amount <= self.balance
    
    def get_withdrawls(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}\n"
            total += item['amount']
        output = title + items + f"Total: {total:.2f}"
        return output

def getTotals(categories):
  total = 0
  breakdown = []
  for category in categories:
    total += category.get_withdrawls()
    breakdown.append(category.get_withdrawls())
  rounded = list(map(lambda x: truncate(x/total), breakdown))
  return rounded
  
def truncate(n):
  multiplier = 10
  return int(n * multiplier) / multiplier


def create_spend_chart(categories): 
  res = "Percentage spent by category\n"
  i = 100
  totals = getTotals(categories)
  while i >= 0:
    cat_spaces = " "
    for total in totals:
        if total * 100 >= i:
            cat_spaces += "o  "
        else:
            cat_spaces += "   "
    res+= str(i).rjust(3) + "|" + cat_spaces + ("\n")
    i-=10
    
  dashes = "-" + "---"*len(categories)
  names = []
  x_axis = ""
  for category in categories:
    names.append(category.name)

  maxi = max(names, key=len)

  for x in range(len(maxi)):
    nameStr = '     '
    for name in names:
          if x >= len(name):
              nameStr += "   "
          else:
              nameStr += name[x] + "  "
    
    if(x != len(maxi) -1 ):
      nameStr += '\n'

      
    x_axis += nameStr

  res+= dashes.rjust(len(dashes)+4) + "\n" + x_axis
  return res