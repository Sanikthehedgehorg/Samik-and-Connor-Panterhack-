import time
def federal_income_tax(income,married):
    tax_brackets = [[0, .0], [11000, .1], [44725, .12], [95375, .22], [182100, .24], [231250, .32], [578125, .35],[0, .37]]
    if married == "Y" or married == "Yes" or married == "yes" or married == "YES" or married == "y":
        for i in range(len(tax_brackets) - 1):
            tax_brackets[i][0] = tax_brackets[i][0] * 2
        tax_brackets[len(tax_brackets) - 1][0] = 1156250
    for x in range(len(tax_brackets)):
        if int(income) < tax_brackets[x][0]:
            index = x
            break
        else:
            index = 7
    total_tax = 0
    if index > 1:
        for y in range(index):
            if y + 1 == index:
                total_tax = total_tax + tax_brackets[y + 1][1] * (tax_brackets[y][0] - int(income))
            else:
                total_tax = total_tax + tax_brackets[y + 1][1] * (tax_brackets[y + 1][0] - tax_brackets[y][0])
            y = y + 1
        return total_tax
    else:
        total_tax = int(income) * 0.1
        return total_tax

def state_income_tax(income,married,state):
    if state == "Alaska" or state == "Florida" or state == "Nevada" or state == "South Dakota" or state == "Tennessee" or state == "Texas" or state == "Wyoming":
        total_tax = 0
        return total_tax
    file = open("state income taxes.txt", "r")
    rates = file.read()
    file.close()
    rateslist = rates.split("\n")
    for i in range(len(rateslist)):
        rateslist[i] = rateslist[i].split(",")
    if married == "Y" or married == "Yes" or married == "yes" or married == "YES" or married == "y":
        for x in range(len(rateslist)):
            if f"{state} married" in rateslist[x]:
                index = x
                found = True
                break
        if x + 1 == len(rateslist):
            print("Can't find state")
            return "error"
            found = False
    else:
        for x in range(len(rateslist)):
            if f"{state} unmarried" in rateslist[x]:
                index = x
                found = True
                break
        if x + 1 == len(rateslist):
            print("Can't find state")
            return "error"
            found = False
    if found == True:
        for i in range(len(rateslist[index]) - 1):
            if int(income) < float(rateslist[index][i + 1]):
                income_index = i + 1
                break
            else:
                income_index = len(rateslist[index]) - 1
            i = i + 1
        broken = True
        total_tax = 0
        if len(rateslist[index]) > 3:
            for y in range(income_index):
                if y + 4 == income_index:
                    total_tax = total_tax + (float(rateslist[index][income_index - 3]) / 100) * (int(income) - float(rateslist[index][income_index - 2]))
                elif broken == True and y + 4 < income_index and y % 2 == 0:
                    total_tax = total_tax + (float(rateslist[index][y + 1]) / 100) * (float(rateslist[index][y + 4]) - float(rateslist[index][y + 2]))
            return total_tax
        else:
            total_tax = (float(rateslist[index][income_index - 1]) / 100) * int(income)
            return total_tax




def Wrapper():
    income = input("Please enter your income for this year: ")
    income = income.replace(",", "")
    married = input("Are you married and filing together? (Y/N): ")
    state = input("Please enter your state of residence: ")
    state = state.title()
    federal_tax = federal_income_tax(income,married)
    state_tax = state_income_tax(income,married,state)
    return federal_tax, state_tax




def property_tax():
    property_value = input("Please enter your property value: ")
    property_value = property_value.replace(",", "")
    property_value = int(property_value)
    county = input("Enter your official county name: ")
    county = county.title()
    file = open("property rates.txt", "r")
    rates = file.read()
    file.close()
    rateslist = rates.split("\n")
    for i in range(len(rateslist)):
        rateslist[i] = rateslist[i].split(",")
    possiblecountylist = []
    for i in range(len(rateslist)):
        if rateslist[i][1] in county:
            possiblecountylist.append(rateslist[i])
    if len(possiblecountylist) > 1:
        countystate = input("Enter the name of your state of residence: ")
        countystate = countystate.title()
        for a in range(len(possiblecountylist)):
            if possiblecountylist[a][0] in countystate:
                tax_rate = possiblecountylist[a][2]
            else:
                print("County and state combination not found, please try again.\n")
                return "error"
            break
    else:
        if len(possiblecountylist) == 1:
            tax_rate = possiblecountylist[0][2]
        if len(possiblecountylist) == 0:
            print("County not recognized, please try again.\n")
            return "error"
    tax_rate = float(tax_rate.replace("%", "")) / 100
    tax = int(property_value * tax_rate)
    return tax

print("Welcome to the tax calculator!\n")
while True:
    option = input("Enter 1 to use the income tax calculator and 2 for the property tax calculator: ")

    if option == "1":
        taxes = Wrapper()
        if taxes[0] == 'error' or taxes[1] == 'error':
            pass
        else:
            time.sleep(0.5)
            print(f"You owe ${taxes[0]:.2f} in federal income taxes and ${taxes[1]:.2f} in state income taxes.\n")
    elif option == "2":
        tax = property_tax()
        if tax == "error":
            pass
        else:
            time.sleep(0.5)
            print(f"You owe ${tax:.2f} in property taxes.\n")