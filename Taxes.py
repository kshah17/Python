print("Welcome to 'My Tax' Calculator")                # title
name = input("Enter name: ")                           # User input name
income = eval(input("Enter Salary (GBP): "))           # User input salary
tax_percentage = eval(input("Enter tax percentage: ")) # User input tax %

tax_rate = (tax_percentage) / 100                      # Works out rate from percentage

tax = income * tax_rate                                # works out tax

tax = '%.2f' % tax                                     # limits figure to 2dp

print (f"The tax {name} owes is {tax} GBP")            # Prints name and tax owed to 2dp







