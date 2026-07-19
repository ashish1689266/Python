actual_cost = float(input(" Please Enter the Actual Product Price: "))
sale_amount = float(input(" Please Enter the Sales Amount: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0} {1} {2} ".format(amount, actual_cost, sale_amount))
else:
    print("No Profit!!!")
