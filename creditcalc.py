import math
import argparse

parser = argparse.ArgumentParser(description="This program calculates a \
specified variable of a differentiated loan")

parser.add_argument("-t", "--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if args.type == "annuity":
    # if they want to know the payment number:
    if args.principal is not None and args.payment is not None and args.interest is not None:
        loan_principal = float(args.principal)
        amount = float(args.payment)
        annual_interest = float(args.interest)
        i = annual_interest / 12 / 100
        if loan_principal < 0 or amount < 0 or annual_interest < 0:
            print("Incorrect parameters")
        else:
            if i == 0:
                output = loan_principal / amount
            else:
                output = math.log(amount/(amount-i*loan_principal), 1+i)  # output is the number of payments

            overpayment = math.ceil(amount) * math.ceil(output) - math.ceil(loan_principal)
            plus = ""
            output_years = ""
            output_month = ""
            year = ""
            month = ""
            if output / 12 >= 1:  # first case: it takes years
                output_years = output // 12
                if output % 12 > 11:
                    output_years = int(output_years + 1)
                else:
                    output_month = math.ceil(output % 12)
                    plus = " and "
                    if output_month == 1:
                        month = " month"
                    else:
                        month = " months"
                if int(output_years) == 1:
                    year = " year"
                else:
                    year = " years"
            elif 0 < output / 12 < 1:  # second case: it takes under 12 month
                output_month = math.ceil(output)
                if output_month == 1:
                    month = " month"
                else:
                    month = " months"
            else:
                print("something went wrong")
            print(f"\nIt will take {output_years}{year}{plus}{output_month}{month} to repay this loan!")
            print(f"Overpayment = {math.ceil(overpayment)}")

    # if they want to know the monthly payment amount:
    elif args.principal is not None and args.periods is not None and args.interest is not None:
        loan_principal = float(args.principal)
        periods = float(args.periods)
        annual_interest = float(args.interest)
        if loan_principal < 0 or periods < 0 or annual_interest < 0:
            print("Incorrect parameters")
        else:
            i = annual_interest / 12 / 100
            amount = loan_principal * ((i*((1+i) ** periods)) / (((1+i) ** periods) - 1))
            overpayment = math.ceil(amount) * math.ceil(periods) - math.ceil(loan_principal)
            print(f"Your annuity payment = {math.ceil(amount)}!")
            print(f"Overpayment = {math.ceil(overpayment)}")

    # if they want to know the loan_principal:
    elif args.periods is not None and args.payment is not None and args.interest is not None:
        amount = float(args.payment)
        periods = float(args.periods)
        annual_interest = float(args.interest)
        i = annual_interest / 12 / 100
        if amount < 0 or periods < 0 or annual_interest < 0:
            print("Incorrect parameters")
        else:
            loan_principal = amount / ((i*(1+i)**periods)/((1+i)**periods-1))
            overpayment = math.ceil(amount) * math.ceil(periods) - int(loan_principal)
            print(f"Your loan principal = {int(loan_principal)}!")
            print(f"Overpayment = {math.ceil(overpayment)}")
    else:
        print("Incorrect parameters}")

elif args.type == "diff":
    if args.principal is not None and args.periods is not None and args.interest is not None and args.payment is None:
        loan_principal = float(args.principal)
        periods = float(args.periods)
        interest = float(args.interest)
        i = interest / 12 / 100
        if loan_principal < 0 or periods < 0 or interest < 0:
            print("Incorrect parameters")
        else:
            overpayment = - loan_principal
            for m in range(int(periods)):
                monthly_amount = loan_principal / periods + i * (loan_principal - ((loan_principal * m) / periods))
                print(f"Month {m + 1}: payment is {math.ceil(monthly_amount)}")
                overpayment += math.ceil(monthly_amount)
            print(f"\nOverpayment = {math.ceil(overpayment)}")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
