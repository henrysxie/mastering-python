num_lemonades = raw_input("How many lemonades did you sell?")
hours = raw_input("How many hours did you work?")

# Cast as integer
try:
    num_lemonades = int(num_lemonades)
    hours = int(hours)
except Exception as e:
    print "Please input valid integer values"
else:
    # Our assumptions
    lemons_per_lemonade = 4
    cost_per_lemon = 0.5
    price = 5

    # Compute profit
    cost = num_lemonades * lemons_per_lemonade * cost_per_lemon

    income = num_lemonades * price

    profit = income - cost

    print "Your profit is ${}".format(profit)
    print "Avg hourly income is ${}".format(profit / hours)
