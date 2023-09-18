
Name = input("Your Name: ")
if len(Name) < 3:
    print("Name must be atleast 3 Characters long!")
elif len(Name) > 25:
    print("Name can be a maximum of 25 long!")
else:
    print("Looks Good!")

loc = str(input("Your Location: "))
if loc == "Karachi" or "karachi":
    print("Salam!")

credit_score = str(input("How is your Credit Score?: "))
if credit_score < str(5):
    print("That's a Shock!")
elif credit_score > str(5):
    print("We Love You!")

if credit_score < str(5):
    credit_status = "Bad"
elif credit_score > str(5):
    credit_status = "Good"

amount = int(input("How much Loan do you want: "))
while amount < 20000:
    print("Amount should be at least 20000")
    break

if credit_status == "Good":
    down_payment: float = 0.1 * amount
    EMI = amount / int(12)
if credit_status == "Bad":
    down_payment: float = 0.2 * amount
    EMI = amount / int(12)
print(f"Hey {Name}!,")
print(f"Your Total Down Payment is: PKR{down_payment}/-")
print(f"Monthly Installment: PKR{EMI}/-")
if amount > 350000 and credit_score < str(5) or amount < 20000:
    print("Status: Not Eligible")
else:
    print("Status: Eligible")

if loc == "Islamabad" or "Dubai":
    print('''
IF ELIGIBLE: 
    ''')
    print("Proceed Online at www.ibsfinance.com")
    print("Or Proceed at your nearest IBS Micro-Finance Kiosk")
print('''
IF NOT ELIGIBLE: 
''')
print("Clear your due funds or Contact Us at www.ibsfinance.com/help")

Exit = input("Type OK to exit > ")
while Exit == "OK":
    break
