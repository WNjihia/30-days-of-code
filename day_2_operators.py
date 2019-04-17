def solve(meal_cost, tip_percent, tax_percent):
    totalCost=(meal_cost +((tip_percent*meal_cost)/100) +((tax_percent*meal_cost)/100))
    print(round(totalCost))

solve(float(input()), int(input()), int(input()))
