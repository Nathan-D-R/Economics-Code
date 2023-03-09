# Description: Simulate the money creation process in a fractional reserve banking system

# Prompt user for initial currency, reserve ratio, and number of banks
print("Input the initial currency in the economy.")
initial_currency = float(input("Initial currency: "))

print("Input the reserve ratio and household reserves, these should be between 0 and 1.")
reserve_ratio = float(input("Reserve ratio: "))
household_reserves = float(input("Household reserves: "))

banks = []

# Create first bank
first_bank_reserves = initial_currency * reserve_ratio
first_bank_deposits = initial_currency * household_reserves
first_bank_loans = initial_currency * (1-reserve_ratio) * (1-household_reserves)
banks.append({
    'reserves': first_bank_reserves,
    'deposits': first_bank_deposits,
    'loans': first_bank_loans
})
money_supply = initial_currency * (1-household_reserves) + first_bank_loans

# For i until new bank reserves are near zero
i = 0
while banks[i]['loans'] >= .001:
    i += 1
    prev_bank = banks[i-1]
    new_bank_reserves = prev_bank['loans'] * reserve_ratio
    new_bank_deposits = prev_bank['loans'] * household_reserves
    new_bank_loans = prev_bank['loans'] * (1-reserve_ratio) * (1-household_reserves)
    banks.append({
        'reserves': new_bank_reserves,
        'deposits': new_bank_deposits,
        'loans': new_bank_loans
    })
    money_supply += new_bank_loans


# Print results for every tenth bank
print(f"Money supply: ${money_supply:.2f}")
for i, bank in enumerate(banks):
    if i % 10 != 0:
        continue
    print(f"Bank {i+1}:")
    print(f"  Reserves: ${bank['reserves']:.2f}")
    print(f"  Deposits: ${bank['deposits']:.2f}")
    print(f"  Loans: ${bank['loans']:.2f}")

# Totals
print(f"The money supply now equals ${money_supply:.2f}")
total_deposits = sum(bank['deposits'] for bank in banks)
print(f"Depositors have ${total_deposits:.2f} in demand deposits.")
total_currency = money_supply - total_deposits
print(f"Borrowers hold ${total_currency:.2f} in currency.")
